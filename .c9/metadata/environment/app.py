{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":18,"column":39},"end":{"row":18,"column":40},"action":"insert","lines":[" "],"id":1471},{"start":{"row":18,"column":40},"end":{"row":18,"column":41},"action":"insert","lines":["g"]},{"start":{"row":18,"column":41},"end":{"row":18,"column":42},"action":"insert","lines":["i"]},{"start":{"row":18,"column":42},"end":{"row":18,"column":43},"action":"insert","lines":["t"]},{"start":{"row":18,"column":43},"end":{"row":18,"column":44},"action":"insert","lines":["h"]},{"start":{"row":18,"column":44},"end":{"row":18,"column":45},"action":"insert","lines":["u"]},{"start":{"row":18,"column":45},"end":{"row":18,"column":46},"action":"insert","lines":["b"]}],[{"start":{"row":42,"column":12},"end":{"row":43,"column":0},"action":"insert","lines":["",""],"id":1472},{"start":{"row":43,"column":0},"end":{"row":43,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":41,"column":0},"end":{"row":44,"column":40},"action":"remove","lines":["@app.route('/login')","def login():","    ","    return render_template(\"login.html\")"],"id":1473},{"start":{"row":41,"column":0},"end":{"row":55,"column":51},"action":"insert","lines":["@app.route('/login', methods=['GET', 'POST'])","def login():","    form = LoginForm()","","    if form.validate_on_submit():","        user = User.query.filter_by(username=form.username.data).first()","        if user:","            if check_password_hash(user.password, form.password.data):","                login_user(user, remember=form.remember.data)","                return redirect(url_for('dashboard'))","","        return '<h1>Invalid username or password</h1>'","        #return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'","","    return render_template('login.html', form=form)"]}],[{"start":{"row":18,"column":0},"end":{"row":18,"column":46},"action":"remove","lines":["#Login Form - taken from Pretty Printed github"],"id":1474}],[{"start":{"row":40,"column":0},"end":{"row":41,"column":0},"action":"insert","lines":["",""],"id":1475}],[{"start":{"row":41,"column":0},"end":{"row":41,"column":46},"action":"insert","lines":["#Login Form - taken from Pretty Printed github"],"id":1476}],[{"start":{"row":2,"column":45},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":1477},{"start":{"row":3,"column":0},"end":{"row":3,"column":1},"action":"insert","lines":["f"]},{"start":{"row":3,"column":1},"end":{"row":3,"column":2},"action":"insert","lines":["r"]},{"start":{"row":3,"column":2},"end":{"row":3,"column":3},"action":"insert","lines":["o"]},{"start":{"row":3,"column":3},"end":{"row":3,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":3,"column":4},"end":{"row":3,"column":5},"action":"insert","lines":[" "],"id":1478},{"start":{"row":3,"column":5},"end":{"row":3,"column":6},"action":"insert","lines":["f"]},{"start":{"row":3,"column":6},"end":{"row":3,"column":7},"action":"insert","lines":["l"]},{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"insert","lines":["a"]},{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"insert","lines":["s"]},{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"insert","lines":["k"]},{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"insert","lines":["_"]}],[{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"insert","lines":["b"],"id":1479},{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"insert","lines":["o"]},{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"insert","lines":["o"]},{"start":{"row":3,"column":14},"end":{"row":3,"column":15},"action":"insert","lines":["t"]},{"start":{"row":3,"column":15},"end":{"row":3,"column":16},"action":"insert","lines":["s"]},{"start":{"row":3,"column":16},"end":{"row":3,"column":17},"action":"insert","lines":["t"]},{"start":{"row":3,"column":17},"end":{"row":3,"column":18},"action":"insert","lines":["r"]},{"start":{"row":3,"column":18},"end":{"row":3,"column":19},"action":"insert","lines":["a"]},{"start":{"row":3,"column":19},"end":{"row":3,"column":20},"action":"insert","lines":["p"]}],[{"start":{"row":3,"column":20},"end":{"row":3,"column":21},"action":"insert","lines":[" "],"id":1480},{"start":{"row":3,"column":21},"end":{"row":3,"column":22},"action":"insert","lines":["i"]},{"start":{"row":3,"column":22},"end":{"row":3,"column":23},"action":"insert","lines":["m"]},{"start":{"row":3,"column":23},"end":{"row":3,"column":24},"action":"insert","lines":["p"]},{"start":{"row":3,"column":24},"end":{"row":3,"column":25},"action":"insert","lines":["o"]},{"start":{"row":3,"column":25},"end":{"row":3,"column":26},"action":"insert","lines":["r"]},{"start":{"row":3,"column":26},"end":{"row":3,"column":27},"action":"insert","lines":["t"]}],[{"start":{"row":3,"column":27},"end":{"row":3,"column":28},"action":"insert","lines":[" "],"id":1481},{"start":{"row":3,"column":28},"end":{"row":3,"column":29},"action":"insert","lines":["B"]},{"start":{"row":3,"column":29},"end":{"row":3,"column":30},"action":"insert","lines":["o"]},{"start":{"row":3,"column":30},"end":{"row":3,"column":31},"action":"insert","lines":["o"]},{"start":{"row":3,"column":31},"end":{"row":3,"column":32},"action":"insert","lines":["t"]},{"start":{"row":3,"column":32},"end":{"row":3,"column":33},"action":"insert","lines":["s"]},{"start":{"row":3,"column":33},"end":{"row":3,"column":34},"action":"insert","lines":["t"]},{"start":{"row":3,"column":34},"end":{"row":3,"column":35},"action":"insert","lines":["r"]},{"start":{"row":3,"column":35},"end":{"row":3,"column":36},"action":"insert","lines":["a"]},{"start":{"row":3,"column":36},"end":{"row":3,"column":37},"action":"insert","lines":["p"]}],[{"start":{"row":12,"column":21},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":1482}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":54},"action":"insert","lines":["app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'"],"id":1483}],[{"start":{"row":13,"column":34},"end":{"row":13,"column":46},"action":"remove","lines":["supposedtobe"],"id":1484}],[{"start":{"row":24,"column":42},"end":{"row":25,"column":0},"action":"insert","lines":["",""],"id":1485},{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"remove","lines":["    "],"id":1486}],[{"start":{"row":25,"column":0},"end":{"row":26,"column":0},"action":"insert","lines":["",""],"id":1487}],[{"start":{"row":26,"column":0},"end":{"row":29,"column":93},"action":"insert","lines":["class RegisterForm(FlaskForm):","    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])","    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])","    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])"],"id":1488}],[{"start":{"row":26,"column":0},"end":{"row":29,"column":93},"action":"remove","lines":["class RegisterForm(FlaskForm):","    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])","    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])","    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])"],"id":1489}],[{"start":{"row":20,"column":0},"end":{"row":21,"column":0},"action":"insert","lines":["",""],"id":1490},{"start":{"row":21,"column":0},"end":{"row":22,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":21,"column":0},"end":{"row":24,"column":93},"action":"insert","lines":["class RegisterForm(FlaskForm):","    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])","    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])","    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])"],"id":1491}],[{"start":{"row":31,"column":0},"end":{"row":32,"column":0},"action":"remove","lines":["",""],"id":1492},{"start":{"row":30,"column":0},"end":{"row":31,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":31,"column":23},"end":{"row":31,"column":24},"action":"remove","lines":["."],"id":1493}],[{"start":{"row":31,"column":23},"end":{"row":31,"column":24},"action":"insert","lines":[" "],"id":1494},{"start":{"row":31,"column":24},"end":{"row":31,"column":25},"action":"insert","lines":["-"]}],[{"start":{"row":31,"column":25},"end":{"row":31,"column":26},"action":"insert","lines":[" "],"id":1495}],[{"start":{"row":31,"column":26},"end":{"row":31,"column":58},"action":"insert","lines":["taken from Pretty Printed github"],"id":1496}],[{"start":{"row":49,"column":0},"end":{"row":63,"column":51},"action":"remove","lines":["@app.route('/login', methods=['GET', 'POST'])","def login():","    form = LoginForm()","","    if form.validate_on_submit():","        user = User.query.filter_by(username=form.username.data).first()","        if user:","            if check_password_hash(user.password, form.password.data):","                login_user(user, remember=form.remember.data)","                return redirect(url_for('dashboard'))","","        return '<h1>Invalid username or password</h1>'","        #return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'","","    return render_template('login.html', form=form)"],"id":1497},{"start":{"row":49,"column":0},"end":{"row":69,"column":37},"action":"insert","lines":["\"\"\"User Login Form\"\"\"","@app.route('/login', methods=['POST', 'GET'])","def login():","    if request.method == 'POST':","        users =mongo.db.users","        login_user = users.find_one({'name' : request.form['username']})","        ","        if login_user:","            if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password']) == login_user['password']:","                session['username'] = request.form['username']","                return redirect(url_for('index'))","            flash('Invalid username/password combination')","    return render_template('login.html')","    ","","","\"\"\"User Logout\"\"\"  ","@app.route('/logout')","def logout():","    session.clear()","    return redirect(url_for('index'))"]}],[{"start":{"row":49,"column":0},"end":{"row":49,"column":21},"action":"remove","lines":["\"\"\"User Login Form\"\"\""],"id":1498},{"start":{"row":48,"column":46},"end":{"row":49,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":62,"column":0},"end":{"row":63,"column":0},"action":"remove","lines":["",""],"id":1499},{"start":{"row":61,"column":4},"end":{"row":62,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":62,"column":0},"end":{"row":62,"column":19},"action":"remove","lines":["\"\"\"User Logout\"\"\"  "],"id":1500},{"start":{"row":62,"column":0},"end":{"row":62,"column":1},"action":"insert","lines":["#"]},{"start":{"row":62,"column":1},"end":{"row":62,"column":2},"action":"insert","lines":["L"]},{"start":{"row":62,"column":2},"end":{"row":62,"column":3},"action":"insert","lines":["o"]},{"start":{"row":62,"column":3},"end":{"row":62,"column":4},"action":"insert","lines":["g"]},{"start":{"row":62,"column":4},"end":{"row":62,"column":5},"action":"insert","lines":["o"]},{"start":{"row":62,"column":5},"end":{"row":62,"column":6},"action":"insert","lines":["u"]},{"start":{"row":62,"column":6},"end":{"row":62,"column":7},"action":"insert","lines":["t"]}],[{"start":{"row":58,"column":41},"end":{"row":58,"column":46},"action":"remove","lines":["index"],"id":1501},{"start":{"row":58,"column":41},"end":{"row":58,"column":42},"action":"insert","lines":["l"]},{"start":{"row":58,"column":42},"end":{"row":58,"column":43},"action":"insert","lines":["o"]},{"start":{"row":58,"column":43},"end":{"row":58,"column":44},"action":"insert","lines":["g"]},{"start":{"row":58,"column":44},"end":{"row":58,"column":45},"action":"insert","lines":["i"]},{"start":{"row":58,"column":45},"end":{"row":58,"column":46},"action":"insert","lines":["n"]}],[{"start":{"row":42,"column":37},"end":{"row":42,"column":42},"action":"remove","lines":["index"],"id":1502},{"start":{"row":42,"column":37},"end":{"row":42,"column":38},"action":"insert","lines":["r"]},{"start":{"row":42,"column":38},"end":{"row":42,"column":39},"action":"insert","lines":["e"]},{"start":{"row":42,"column":39},"end":{"row":42,"column":40},"action":"insert","lines":["g"]},{"start":{"row":42,"column":40},"end":{"row":42,"column":41},"action":"insert","lines":["i"]},{"start":{"row":42,"column":41},"end":{"row":42,"column":42},"action":"insert","lines":["s"]},{"start":{"row":42,"column":42},"end":{"row":42,"column":43},"action":"insert","lines":["t"]},{"start":{"row":42,"column":43},"end":{"row":42,"column":44},"action":"insert","lines":["e"]},{"start":{"row":42,"column":44},"end":{"row":42,"column":45},"action":"insert","lines":["r"]}],[{"start":{"row":58,"column":41},"end":{"row":58,"column":46},"action":"remove","lines":["login"],"id":1503},{"start":{"row":58,"column":41},"end":{"row":58,"column":42},"action":"insert","lines":["t"]},{"start":{"row":58,"column":42},"end":{"row":58,"column":43},"action":"insert","lines":["e"]},{"start":{"row":58,"column":43},"end":{"row":58,"column":44},"action":"insert","lines":["r"]},{"start":{"row":58,"column":44},"end":{"row":58,"column":45},"action":"insert","lines":["m"]},{"start":{"row":58,"column":45},"end":{"row":58,"column":46},"action":"insert","lines":["s"]}],[{"start":{"row":58,"column":41},"end":{"row":58,"column":42},"action":"insert","lines":["g"],"id":1504},{"start":{"row":58,"column":42},"end":{"row":58,"column":43},"action":"insert","lines":["e"]},{"start":{"row":58,"column":43},"end":{"row":58,"column":44},"action":"insert","lines":["t"]},{"start":{"row":58,"column":44},"end":{"row":58,"column":45},"action":"insert","lines":["_"]}],[{"start":{"row":68,"column":0},"end":{"row":68,"column":15},"action":"remove","lines":["@app.route('/')"],"id":1505}],[{"start":{"row":49,"column":0},"end":{"row":50,"column":0},"action":"insert","lines":["",""],"id":1506}],[{"start":{"row":49,"column":0},"end":{"row":49,"column":15},"action":"insert","lines":["@app.route('/')"],"id":1507}],[{"start":{"row":19,"column":0},"end":{"row":20,"column":0},"action":"insert","lines":["",""],"id":1508}],[{"start":{"row":20,"column":0},"end":{"row":24,"column":39},"action":"insert","lines":["class User(UserMixin, db.Model):","    id = db.Column(db.Integer, primary_key=True)","    username = db.Column(db.String(15), unique=True)","    email = db.Column(db.String(50), unique=True)","    password = db.Column(db.String(80))"],"id":1509}],[{"start":{"row":20,"column":0},"end":{"row":25,"column":0},"action":"remove","lines":["class User(UserMixin, db.Model):","    id = db.Column(db.Integer, primary_key=True)","    username = db.Column(db.String(15), unique=True)","    email = db.Column(db.String(50), unique=True)","    password = db.Column(db.String(80))",""],"id":1510}],[{"start":{"row":20,"column":0},"end":{"row":21,"column":0},"action":"insert","lines":["",""],"id":1511}],[{"start":{"row":68,"column":29},"end":{"row":68,"column":34},"action":"remove","lines":["index"],"id":1512},{"start":{"row":68,"column":29},"end":{"row":68,"column":30},"action":"insert","lines":["l"]},{"start":{"row":68,"column":30},"end":{"row":68,"column":31},"action":"insert","lines":["o"]},{"start":{"row":68,"column":31},"end":{"row":68,"column":32},"action":"insert","lines":["g"]},{"start":{"row":68,"column":32},"end":{"row":68,"column":33},"action":"insert","lines":["i"]},{"start":{"row":68,"column":33},"end":{"row":68,"column":34},"action":"insert","lines":["n"]}],[{"start":{"row":108,"column":41},"end":{"row":109,"column":0},"action":"insert","lines":["",""],"id":1513},{"start":{"row":109,"column":0},"end":{"row":109,"column":4},"action":"insert","lines":["    "]},{"start":{"row":109,"column":4},"end":{"row":110,"column":0},"action":"insert","lines":["",""]},{"start":{"row":110,"column":0},"end":{"row":110,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":110,"column":0},"end":{"row":110,"column":4},"action":"remove","lines":["    "],"id":1514}],[{"start":{"row":110,"column":0},"end":{"row":110,"column":1},"action":"insert","lines":["@"],"id":1515},{"start":{"row":110,"column":1},"end":{"row":110,"column":2},"action":"insert","lines":["a"]},{"start":{"row":110,"column":2},"end":{"row":110,"column":3},"action":"insert","lines":["p"]},{"start":{"row":110,"column":3},"end":{"row":110,"column":4},"action":"insert","lines":["p"]},{"start":{"row":110,"column":4},"end":{"row":110,"column":5},"action":"insert","lines":["."]},{"start":{"row":110,"column":5},"end":{"row":110,"column":6},"action":"insert","lines":["r"]},{"start":{"row":110,"column":6},"end":{"row":110,"column":7},"action":"insert","lines":["o"]},{"start":{"row":110,"column":7},"end":{"row":110,"column":8},"action":"insert","lines":["u"]},{"start":{"row":110,"column":8},"end":{"row":110,"column":9},"action":"insert","lines":["t"]},{"start":{"row":110,"column":9},"end":{"row":110,"column":10},"action":"insert","lines":["e"]}],[{"start":{"row":110,"column":10},"end":{"row":110,"column":12},"action":"insert","lines":["()"],"id":1516}],[{"start":{"row":110,"column":11},"end":{"row":110,"column":12},"action":"insert","lines":["/"],"id":1517},{"start":{"row":110,"column":12},"end":{"row":110,"column":13},"action":"insert","lines":["v"]},{"start":{"row":110,"column":13},"end":{"row":110,"column":14},"action":"insert","lines":["o"]},{"start":{"row":110,"column":14},"end":{"row":110,"column":15},"action":"insert","lines":["t"]},{"start":{"row":110,"column":15},"end":{"row":110,"column":16},"action":"insert","lines":["e"]}],[{"start":{"row":110,"column":16},"end":{"row":110,"column":17},"action":"insert","lines":["'"],"id":1518}],[{"start":{"row":110,"column":11},"end":{"row":110,"column":12},"action":"insert","lines":["'"],"id":1519}],[{"start":{"row":110,"column":19},"end":{"row":111,"column":0},"action":"insert","lines":["",""],"id":1520}],[{"start":{"row":111,"column":0},"end":{"row":111,"column":1},"action":"insert","lines":["d"],"id":1521}],[{"start":{"row":111,"column":0},"end":{"row":111,"column":1},"action":"remove","lines":["d"],"id":1522},{"start":{"row":111,"column":0},"end":{"row":111,"column":3},"action":"insert","lines":["def"]}],[{"start":{"row":111,"column":3},"end":{"row":111,"column":4},"action":"insert","lines":[" "],"id":1523},{"start":{"row":111,"column":4},"end":{"row":111,"column":5},"action":"insert","lines":["v"]},{"start":{"row":111,"column":5},"end":{"row":111,"column":6},"action":"insert","lines":["o"]},{"start":{"row":111,"column":6},"end":{"row":111,"column":7},"action":"insert","lines":["t"]},{"start":{"row":111,"column":7},"end":{"row":111,"column":8},"action":"insert","lines":["e"]}],[{"start":{"row":111,"column":8},"end":{"row":111,"column":10},"action":"insert","lines":["()"],"id":1524}],[{"start":{"row":111,"column":9},"end":{"row":111,"column":10},"action":"insert","lines":["t"],"id":1525},{"start":{"row":111,"column":10},"end":{"row":111,"column":11},"action":"insert","lines":["e"]},{"start":{"row":111,"column":11},"end":{"row":111,"column":12},"action":"insert","lines":["r"]},{"start":{"row":111,"column":12},"end":{"row":111,"column":13},"action":"insert","lines":["m"]}],[{"start":{"row":111,"column":9},"end":{"row":111,"column":13},"action":"remove","lines":["term"],"id":1526},{"start":{"row":111,"column":9},"end":{"row":111,"column":16},"action":"insert","lines":["term_id"]}],[{"start":{"row":111,"column":9},"end":{"row":111,"column":16},"action":"remove","lines":["term_id"],"id":1527}],[{"start":{"row":111,"column":10},"end":{"row":111,"column":11},"action":"insert","lines":[":"],"id":1528}],[{"start":{"row":111,"column":11},"end":{"row":112,"column":0},"action":"insert","lines":["",""],"id":1529},{"start":{"row":112,"column":0},"end":{"row":112,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":109,"column":2},"end":{"row":109,"column":3},"action":"remove","lines":[" "],"id":1530},{"start":{"row":109,"column":1},"end":{"row":109,"column":2},"action":"remove","lines":[" "]},{"start":{"row":109,"column":0},"end":{"row":109,"column":1},"action":"remove","lines":[" "]}],[{"start":{"row":109,"column":0},"end":{"row":110,"column":0},"action":"insert","lines":["",""],"id":1531},{"start":{"row":110,"column":0},"end":{"row":110,"column":1},"action":"insert","lines":["#"]},{"start":{"row":110,"column":1},"end":{"row":110,"column":2},"action":"insert","lines":["A"]},{"start":{"row":110,"column":2},"end":{"row":110,"column":3},"action":"insert","lines":["d"]},{"start":{"row":110,"column":3},"end":{"row":110,"column":4},"action":"insert","lines":["d"]}],[{"start":{"row":110,"column":3},"end":{"row":110,"column":4},"action":"remove","lines":["d"],"id":1532},{"start":{"row":110,"column":2},"end":{"row":110,"column":3},"action":"remove","lines":["d"]},{"start":{"row":110,"column":1},"end":{"row":110,"column":2},"action":"remove","lines":["A"]}],[{"start":{"row":110,"column":1},"end":{"row":110,"column":2},"action":"insert","lines":["V"],"id":1533},{"start":{"row":110,"column":2},"end":{"row":110,"column":3},"action":"insert","lines":["o"]},{"start":{"row":110,"column":3},"end":{"row":110,"column":4},"action":"insert","lines":["t"]},{"start":{"row":110,"column":4},"end":{"row":110,"column":5},"action":"insert","lines":["e"]}],[{"start":{"row":110,"column":5},"end":{"row":110,"column":6},"action":"insert","lines":[" "],"id":1534},{"start":{"row":110,"column":6},"end":{"row":110,"column":7},"action":"insert","lines":["f"]},{"start":{"row":110,"column":7},"end":{"row":110,"column":8},"action":"insert","lines":["u"]},{"start":{"row":110,"column":8},"end":{"row":110,"column":9},"action":"insert","lines":["n"]},{"start":{"row":110,"column":9},"end":{"row":110,"column":10},"action":"insert","lines":["c"]},{"start":{"row":110,"column":10},"end":{"row":110,"column":11},"action":"insert","lines":["t"]},{"start":{"row":110,"column":11},"end":{"row":110,"column":12},"action":"insert","lines":["i"]},{"start":{"row":110,"column":12},"end":{"row":110,"column":13},"action":"insert","lines":["o"]},{"start":{"row":110,"column":13},"end":{"row":110,"column":14},"action":"insert","lines":["n"]},{"start":{"row":110,"column":14},"end":{"row":110,"column":15},"action":"insert","lines":["a"]},{"start":{"row":110,"column":15},"end":{"row":110,"column":16},"action":"insert","lines":["l"]},{"start":{"row":110,"column":16},"end":{"row":110,"column":17},"action":"insert","lines":["i"]},{"start":{"row":110,"column":17},"end":{"row":110,"column":18},"action":"insert","lines":["t"]},{"start":{"row":110,"column":18},"end":{"row":110,"column":19},"action":"insert","lines":["y"]}],[{"start":{"row":110,"column":19},"end":{"row":110,"column":20},"action":"insert","lines":[" "],"id":1535}],[{"start":{"row":113,"column":4},"end":{"row":113,"column":5},"action":"insert","lines":["r"],"id":1536},{"start":{"row":113,"column":5},"end":{"row":113,"column":6},"action":"insert","lines":["e"]},{"start":{"row":113,"column":6},"end":{"row":113,"column":7},"action":"insert","lines":["t"]},{"start":{"row":113,"column":7},"end":{"row":113,"column":8},"action":"insert","lines":["u"]},{"start":{"row":113,"column":8},"end":{"row":113,"column":9},"action":"insert","lines":["r"]},{"start":{"row":113,"column":9},"end":{"row":113,"column":10},"action":"insert","lines":["n"]}],[{"start":{"row":113,"column":10},"end":{"row":113,"column":11},"action":"insert","lines":[" "],"id":1537},{"start":{"row":113,"column":11},"end":{"row":113,"column":12},"action":"insert","lines":["r"]},{"start":{"row":113,"column":12},"end":{"row":113,"column":13},"action":"insert","lines":["e"]},{"start":{"row":113,"column":13},"end":{"row":113,"column":14},"action":"insert","lines":["d"]}],[{"start":{"row":113,"column":11},"end":{"row":113,"column":14},"action":"remove","lines":["red"],"id":1538},{"start":{"row":113,"column":11},"end":{"row":113,"column":19},"action":"insert","lines":["redirect"]}],[{"start":{"row":113,"column":19},"end":{"row":113,"column":21},"action":"insert","lines":["()"],"id":1539}],[{"start":{"row":113,"column":20},"end":{"row":113,"column":21},"action":"insert","lines":["u"],"id":1540},{"start":{"row":113,"column":21},"end":{"row":113,"column":22},"action":"insert","lines":["r"]},{"start":{"row":113,"column":22},"end":{"row":113,"column":23},"action":"insert","lines":["l"]}],[{"start":{"row":113,"column":20},"end":{"row":113,"column":23},"action":"remove","lines":["url"],"id":1541},{"start":{"row":113,"column":20},"end":{"row":113,"column":27},"action":"insert","lines":["url_for"]}],[{"start":{"row":113,"column":27},"end":{"row":113,"column":29},"action":"insert","lines":["()"],"id":1542}],[{"start":{"row":113,"column":28},"end":{"row":113,"column":30},"action":"insert","lines":["''"],"id":1543}],[{"start":{"row":113,"column":29},"end":{"row":113,"column":30},"action":"insert","lines":["v"],"id":1544},{"start":{"row":113,"column":30},"end":{"row":113,"column":31},"action":"insert","lines":["o"]},{"start":{"row":113,"column":31},"end":{"row":113,"column":32},"action":"insert","lines":["t"]},{"start":{"row":113,"column":32},"end":{"row":113,"column":33},"action":"insert","lines":["e"]}],[{"start":{"row":113,"column":11},"end":{"row":113,"column":35},"action":"remove","lines":["redirect(url_for('vote')"],"id":1545},{"start":{"row":113,"column":11},"end":{"row":113,"column":12},"action":"insert","lines":["r"]},{"start":{"row":113,"column":12},"end":{"row":113,"column":13},"action":"insert","lines":["e"]}],[{"start":{"row":113,"column":11},"end":{"row":113,"column":13},"action":"remove","lines":["re"],"id":1546},{"start":{"row":113,"column":11},"end":{"row":113,"column":26},"action":"insert","lines":["render_template"]}],[{"start":{"row":113,"column":26},"end":{"row":113,"column":28},"action":"insert","lines":["()"],"id":1547}],[{"start":{"row":113,"column":27},"end":{"row":113,"column":28},"action":"remove","lines":[")"],"id":1548}],[{"start":{"row":113,"column":27},"end":{"row":113,"column":28},"action":"insert","lines":["t"],"id":1549},{"start":{"row":113,"column":28},"end":{"row":113,"column":29},"action":"insert","lines":["e"]},{"start":{"row":113,"column":29},"end":{"row":113,"column":30},"action":"insert","lines":["r"]}],[{"start":{"row":113,"column":29},"end":{"row":113,"column":30},"action":"remove","lines":["r"],"id":1550},{"start":{"row":113,"column":28},"end":{"row":113,"column":29},"action":"remove","lines":["e"]},{"start":{"row":113,"column":27},"end":{"row":113,"column":28},"action":"remove","lines":["t"]}],[{"start":{"row":113,"column":27},"end":{"row":113,"column":28},"action":"insert","lines":["v"],"id":1551},{"start":{"row":113,"column":28},"end":{"row":113,"column":29},"action":"insert","lines":["o"]},{"start":{"row":113,"column":29},"end":{"row":113,"column":30},"action":"insert","lines":["t"]},{"start":{"row":113,"column":30},"end":{"row":113,"column":31},"action":"insert","lines":["e"]},{"start":{"row":113,"column":31},"end":{"row":113,"column":32},"action":"insert","lines":["."]},{"start":{"row":113,"column":32},"end":{"row":113,"column":33},"action":"insert","lines":["h"]},{"start":{"row":113,"column":33},"end":{"row":113,"column":34},"action":"insert","lines":["t"]},{"start":{"row":113,"column":34},"end":{"row":113,"column":35},"action":"insert","lines":["m"]},{"start":{"row":113,"column":35},"end":{"row":113,"column":36},"action":"insert","lines":["l"]}],[{"start":{"row":111,"column":17},"end":{"row":111,"column":27},"action":"insert","lines":["/<term_id>"],"id":1552}],[{"start":{"row":113,"column":27},"end":{"row":113,"column":28},"action":"insert","lines":["'"],"id":1553}],[{"start":{"row":113,"column":37},"end":{"row":113,"column":38},"action":"insert","lines":["'"],"id":1554}],[{"start":{"row":111,"column":17},"end":{"row":111,"column":28},"action":"remove","lines":["/<term_id>'"],"id":1555}],[{"start":{"row":111,"column":18},"end":{"row":112,"column":0},"action":"insert","lines":["",""],"id":1556}],[{"start":{"row":111,"column":18},"end":{"row":112,"column":0},"action":"remove","lines":["",""],"id":1557}],[{"start":{"row":113,"column":27},"end":{"row":113,"column":28},"action":"insert","lines":["u"],"id":1558},{"start":{"row":113,"column":28},"end":{"row":113,"column":29},"action":"insert","lines":["r"]},{"start":{"row":113,"column":29},"end":{"row":113,"column":30},"action":"insert","lines":["l"]}],[{"start":{"row":113,"column":27},"end":{"row":113,"column":30},"action":"remove","lines":["url"],"id":1559},{"start":{"row":113,"column":27},"end":{"row":113,"column":34},"action":"insert","lines":["url_for"]}],[{"start":{"row":113,"column":34},"end":{"row":113,"column":35},"action":"insert","lines":["("],"id":1560}],[{"start":{"row":113,"column":46},"end":{"row":113,"column":47},"action":"insert","lines":[")"],"id":1561}],[{"start":{"row":113,"column":11},"end":{"row":113,"column":26},"action":"remove","lines":["render_template"],"id":1563},{"start":{"row":113,"column":11},"end":{"row":113,"column":12},"action":"insert","lines":["r"]},{"start":{"row":113,"column":12},"end":{"row":113,"column":13},"action":"insert","lines":["e"]},{"start":{"row":113,"column":13},"end":{"row":113,"column":14},"action":"insert","lines":["d"]},{"start":{"row":113,"column":14},"end":{"row":113,"column":15},"action":"insert","lines":["i"]},{"start":{"row":113,"column":15},"end":{"row":113,"column":16},"action":"insert","lines":["r"]},{"start":{"row":113,"column":16},"end":{"row":113,"column":17},"action":"insert","lines":["e"]},{"start":{"row":113,"column":17},"end":{"row":113,"column":18},"action":"insert","lines":["c"]},{"start":{"row":113,"column":18},"end":{"row":113,"column":19},"action":"insert","lines":["t"]}],[{"start":{"row":111,"column":17},"end":{"row":111,"column":18},"action":"insert","lines":["'"],"id":1564}],[{"start":{"row":113,"column":11},"end":{"row":113,"column":19},"action":"remove","lines":["redirect"],"id":1565},{"start":{"row":113,"column":11},"end":{"row":113,"column":12},"action":"insert","lines":["r"]},{"start":{"row":113,"column":12},"end":{"row":113,"column":13},"action":"insert","lines":["e"]},{"start":{"row":113,"column":13},"end":{"row":113,"column":14},"action":"insert","lines":["d"]}],[{"start":{"row":113,"column":13},"end":{"row":113,"column":14},"action":"remove","lines":["d"],"id":1566}],[{"start":{"row":113,"column":13},"end":{"row":113,"column":14},"action":"insert","lines":["n"],"id":1567},{"start":{"row":113,"column":14},"end":{"row":113,"column":15},"action":"insert","lines":["d"]}],[{"start":{"row":113,"column":11},"end":{"row":113,"column":15},"action":"remove","lines":["rend"],"id":1568},{"start":{"row":113,"column":11},"end":{"row":113,"column":26},"action":"insert","lines":["render_template"]}],[{"start":{"row":113,"column":27},"end":{"row":113,"column":35},"action":"remove","lines":["url_for("],"id":1569}],[{"start":{"row":113,"column":38},"end":{"row":113,"column":39},"action":"remove","lines":[")"],"id":1570}],[{"start":{"row":111,"column":17},"end":{"row":111,"column":18},"action":"insert","lines":["/"],"id":1571}],[{"start":{"row":111,"column":17},"end":{"row":111,"column":18},"action":"remove","lines":["/"],"id":1572}]]},"ace":{"folds":[],"scrolltop":1321,"scrollleft":0,"selection":{"start":{"row":111,"column":17},"end":{"row":111,"column":17},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":81,"state":"start","mode":"ace/mode/python"}},"timestamp":1565948918465,"hash":"dd4dc706286f3a2709ef5ee8bdc4e9780e2765bc"}