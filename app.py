from flask import Flask, redirect, url_for, render_template, request, flash
from models import db, Assignment
from forms import AssignmentForm
import pprint

# Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'appleisthedefinitionofinnovation'
app.config['DEBUG'] = False

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///assignment.sqlite'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/book'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route("/")
def index():
    '''
    Home page
    '''

    #! IF datetime.date is 2 days ago
        #! Delete it
        
    return redirect(url_for('planner'))
    #return redirect(url_for('planner'))

@app.route("/planner")
def planner():
    '''
    Planner Page
    '''
    data = {}
    assignments = Assignment.query.order_by(Assignment.assignmtDate).all()
    for assignment in assignments:
        
        if assignment.assignmtDate in data.keys():
            data[assignment.assignmtDate].append([assignment.assignmtDate, assignment.assignmtClass, assignment.assignmtInfo])

        else:
            #data.update({assignment.assignmtDate:assignment.assignmtClass})
            #data[assignment.assignmtDate].append([assignment.assignmtInfo, assignment.assignmtClass])
            data.setdefault(assignment.assignmtDate,[]).append([assignment.assignmtDate, assignment.assignmtClass, assignment.assignmtInfo])
    
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(data)

    x = list(data.keys())

    #! Make list of assignmnent.assignmtDate
    #! if var/duplicate in list
    #! then combine

    return render_template('web/planner.html', assignments=assignments, data=data, x=x)

@app.route("/new_assignment", methods=('GET', 'POST'))
def new_assignment():
    '''
    Create new assignment
    '''
    form = AssignmentForm()
    if form.validate_on_submit():
        my_assignment = Assignment()
        form.populate_obj(my_assignment)
        db.session.add(my_assignment)
        try:
            db.session.commit()
            # User info
            flash('Assignment created correctly', 'success')
            return redirect(url_for('assignments'))
        except:
            db.session.rollback()
            flash('Error generating assignment.', 'danger')

    return render_template('web/new_assignment.html', form=form)


@app.route("/edit_assignment/<id>", methods=('GET', 'POST'))
def edit_assignment(id):
    '''
    Edit assignment

    :param id: Id from assignment
    '''
    my_assignment = Assignment.query.filter_by(id=id).first()
    form = AssignmentForm(obj=my_assignment)
    if form.validate_on_submit():
        try:
            # Update assignment
            form.populate_obj(my_assignment)
            db.session.add(my_assignment)
            db.session.commit()
            # User info
            flash('Saved successfully', 'success')
        except:
            db.session.rollback()
            flash('Error update assignment.', 'danger')
            
    return render_template(
        'web/edit_assignment.html',
        form=form)


@app.route("/assignments")
def assignments():
    '''
    Show alls assignments
    '''
    assignments = Assignment.query.order_by(Assignment.assignmtDate).all()
    return render_template('web/assignments.html', assignments=assignments)


@app.route("/search")
def search():
    '''
    Search
    '''
    class_search = request.args.get('assignmtClass')
    all_assignments = Assignment.query.filter(
        Assignment.assignmtClass.contains(class_search)
        ).order_by(Assignment.assignmtClass).all()
    return render_template('web/assignments.html', assignments=all_assignments)


@app.route("/assignments/delete", methods=('POST',))
def assignments_delete():
    '''
    Delete assignment
    '''
    try:
        my_assignment = Assignment.query.filter_by(id=request.form['id']).first()
        db.session.delete(my_assignment)
        db.session.commit()
        flash('Delete successfully.', 'danger')
    except:
        db.session.rollback()
        flash('Error delete  assignment.', 'danger')

    return redirect(url_for('assignments'))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
