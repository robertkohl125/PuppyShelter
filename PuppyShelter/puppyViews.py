from PuppyShelter import app, models, forms
from flask import render_template, url_for, request, redirect, flash, jsonify
import logging 
from math import ceil
from flask import session as login_session

logging.info('puppyViews.py file accessed ')


class Pagination(object):
    def __init__(self, page, PER_PAGE, total_count):
        self.page = page
        self.per_page = PER_PAGE
        self.total_count = total_count
    @property
    def pages(self):
        return int(ceil(self.total_count / float(self.per_page)))
    @property
    def has_prev(self):
        return self.page > 1
    @property
    def has_next(self):
        return self.page < self.pages
    def iter_pages(self, left_edge=2, left_current=2, right_current=5, right_edge=2):
        last = 0
        for num in xrange(1, self.pages + 1):
            if num <= left_edge \
                or (num > self.page - left_current - 1 and num < self.page + right_current) \
                or num > self.pages - right_edge:
                if last + 1 != num:
                    yield None
                yield num
                last = num



@app.route('/puppies/', defaults={'page': 1})
@app.route('/puppies/page/<int:page>')
def puppies(page):
    PER_PAGE = 5
    total_count = models.countPuppies()
    puppies = models.paginatePuppies(page, PER_PAGE, total_count)
    if not puppies and page != 1:
        abort(404)
    pagination = Pagination(page, PER_PAGE, total_count)

    def url_for_other_page(page):
        args = request.view_args.copy()
        args['page'] = page
        return url_for(request.endpoint, **args)
    app.jinja_env.globals['url_for_other_page'] = url_for_other_page
    return render_template('puppyAll.html', 
        pagination=pagination,
        puppies = puppies)
#
@app.route('/puppies/<int:puppy_id>/puppyview/')
def puppyView(puppy_id):
    puppy = models.selectAllPuppies().filter_by(puppy_id = puppy_id)
    owner = models.selectAdopterOwners(puppy_id)
    shelter = models.selectEnrolledShelter(puppy_id)
    a = models.selectAdopterOwners(puppy_id).scalar()
    for p in puppy:
        print p.picture
    if a is None:
        txt1 = 'Adopt'
        txt2 = ''
        btn = 'success'
        att = 'enabled'
    else:
        txt1 = ''
        txt2 = 'was already adopted'
        btn = 'danger'
        att = 'disabled'
    return render_template('puppyView.html', 
        puppy = puppy, 
        puppy_id = puppy_id, 
        shelter = shelter, 
        owner = owner, 
        txt1 = txt1,
        txt2 = txt2,
        att = att, 
        btn = btn)


#
@app.route('/puppies/puppynew', methods = ['GET','POST'])
def puppyNew():
    if 'username' not in login_session:
        return render_template('unauthorized.html')
    else:
        print login_session['username']
        shelter_choices = models.selectAvailableShelters()
        form = forms.PuppyForm(request.form, obj = shelter_choices)
        form.shelter_id.choices = [(a.shelter_id, a.name) for a in shelter_choices]
        print form.shelter_id.choices
        if request.method == "POST" and form.validate():
            new_puppy = {
                'name': form.name.data,
                'gender': form.gender.data,
                'dateOfbirth': form.dateOfbirth.data,
                'picture': form.picture.data,
                'breed': form.breed.data,
                'weight': form.weight.data,
                'shelter_id': form.shelter_id.data}
            models.createPuppy(new_puppy)
            flash('A new puppy is ready for adoption!')
            return redirect(url_for('puppies'))
        else:
            return render_template('puppyNew.html', 
                form = form)


#
@app.route('/puppies/<int:puppy_id>/puppyedit', methods = ['GET','POST'])
def puppyEdit(puppy_id):
    if 'username' not in login_session:
        return render_template('unauthorized.html')
    else:
        shelter_choices = models.selectAvailableShelters()
        form = forms.PuppyForm(request.form, obj = shelter_choices)
        form.shelter_id.choices = [(a.shelter_id, a.name) for a in shelter_choices]
        puppy = models.selectAllPuppies().filter_by(puppy_id=puppy_id)
        shelter = models.selectEnrolledShelter(puppy_id)
        if request.method == "POST" and form.validate():
            edit_puppy = {
                'name': form.name.data,
                'gender': form.gender.data,
                'dateOfbirth': form.dateOfbirth.data,
                'picture': form.picture.data,
                'breed': form.breed.data,
                'weight': form.weight.data,
                'shelter_id': form.shelter_id.data}
            models.editPuppy(edit_puppy, puppy_id)
            return redirect(url_for('puppies'))
        else:
            return render_template('puppyEdit.html', 
                puppy = puppy, 
                puppy_id = puppy_id, 
                shelter = shelter,
                form = form)


#
@app.route('/puppies/<int:puppy_id>/puppydelete', methods = ['GET','POST'])
def puppyDelete(puppy_id):
    if 'username' not in login_session:
        return render_template('unauthorized.html')
    else:
        puppy = models.selectAllPuppies().filter_by(puppy_id=puppy_id)
        if request.method == "POST":
            models.deletePuppy(puppy_id)
            return redirect(url_for('puppies'))
        else:
            return render_template('puppyDelete.html', 
                puppy = puppy, 
                puppy_id = puppy_id)

app.secret_key = 'super_secret_key'