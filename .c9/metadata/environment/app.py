{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":94,"column":14},"end":{"row":94,"column":25},"action":"remove","lines":["search_term"],"id":134}],[{"start":{"row":95,"column":4},"end":{"row":97,"column":65},"action":"remove","lines":["search_term= = {'term_name': request.form.get('term_name')},","    mongo.db.terms.find({ \"$text\": { \"$search\": search_term } })","    return render_template(\"searchresults.html\", results=results)"],"id":135}],[{"start":{"row":95,"column":4},"end":{"row":98,"column":36},"action":"insert","lines":["def edit_category(category_id):","    return render_template('editcategory.html',","    category=mongo.db.categories.find_one(","    {'_id': ObjectId(category_id)}))"],"id":136}],[{"start":{"row":94,"column":14},"end":{"row":94,"column":15},"action":"insert","lines":["t"],"id":137},{"start":{"row":94,"column":15},"end":{"row":94,"column":16},"action":"insert","lines":["e"]},{"start":{"row":94,"column":16},"end":{"row":94,"column":17},"action":"insert","lines":["r"]},{"start":{"row":94,"column":17},"end":{"row":94,"column":18},"action":"insert","lines":["m"]},{"start":{"row":94,"column":18},"end":{"row":94,"column":19},"action":"insert","lines":["_"]},{"start":{"row":94,"column":19},"end":{"row":94,"column":20},"action":"insert","lines":["n"]}],[{"start":{"row":94,"column":20},"end":{"row":94,"column":21},"action":"insert","lines":["a"],"id":138},{"start":{"row":94,"column":21},"end":{"row":94,"column":22},"action":"insert","lines":["m"]},{"start":{"row":94,"column":22},"end":{"row":94,"column":23},"action":"insert","lines":["e"]}],[{"start":{"row":95,"column":4},"end":{"row":95,"column":35},"action":"remove","lines":["def edit_category(category_id):"],"id":139},{"start":{"row":95,"column":0},"end":{"row":95,"column":4},"action":"remove","lines":["    "]},{"start":{"row":94,"column":25},"end":{"row":95,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":95,"column":28},"end":{"row":95,"column":40},"action":"remove","lines":["editcategory"],"id":140},{"start":{"row":95,"column":28},"end":{"row":95,"column":29},"action":"insert","lines":["s"]},{"start":{"row":95,"column":29},"end":{"row":95,"column":30},"action":"insert","lines":["e"]},{"start":{"row":95,"column":30},"end":{"row":95,"column":31},"action":"insert","lines":["a"]},{"start":{"row":95,"column":31},"end":{"row":95,"column":32},"action":"insert","lines":["r"]},{"start":{"row":95,"column":32},"end":{"row":95,"column":33},"action":"insert","lines":["c"]},{"start":{"row":95,"column":33},"end":{"row":95,"column":34},"action":"insert","lines":["h"]},{"start":{"row":95,"column":34},"end":{"row":95,"column":35},"action":"insert","lines":["r"]},{"start":{"row":95,"column":35},"end":{"row":95,"column":36},"action":"insert","lines":["e"]},{"start":{"row":95,"column":36},"end":{"row":95,"column":37},"action":"insert","lines":["s"]},{"start":{"row":95,"column":37},"end":{"row":95,"column":38},"action":"insert","lines":["u"]},{"start":{"row":95,"column":38},"end":{"row":95,"column":39},"action":"insert","lines":["l"]},{"start":{"row":95,"column":39},"end":{"row":95,"column":40},"action":"insert","lines":["t"]},{"start":{"row":95,"column":40},"end":{"row":95,"column":41},"action":"insert","lines":["s"]}],[{"start":{"row":96,"column":4},"end":{"row":96,"column":12},"action":"remove","lines":["category"],"id":141},{"start":{"row":96,"column":4},"end":{"row":96,"column":5},"action":"insert","lines":["t"]},{"start":{"row":96,"column":5},"end":{"row":96,"column":6},"action":"insert","lines":["e"]},{"start":{"row":96,"column":6},"end":{"row":96,"column":7},"action":"insert","lines":["r"]}],[{"start":{"row":96,"column":7},"end":{"row":96,"column":8},"action":"insert","lines":["m"],"id":142}],[{"start":{"row":97,"column":6},"end":{"row":97,"column":9},"action":"remove","lines":["_id"],"id":143},{"start":{"row":97,"column":6},"end":{"row":97,"column":7},"action":"insert","lines":["t"]},{"start":{"row":97,"column":7},"end":{"row":97,"column":8},"action":"insert","lines":["e"]},{"start":{"row":97,"column":8},"end":{"row":97,"column":9},"action":"insert","lines":["r"]},{"start":{"row":97,"column":9},"end":{"row":97,"column":10},"action":"insert","lines":["m"]}],[{"start":{"row":97,"column":6},"end":{"row":97,"column":10},"action":"remove","lines":["term"],"id":144},{"start":{"row":97,"column":6},"end":{"row":97,"column":15},"action":"insert","lines":["term_name"]}],[{"start":{"row":97,"column":27},"end":{"row":97,"column":38},"action":"remove","lines":["category_id"],"id":145},{"start":{"row":97,"column":27},"end":{"row":97,"column":28},"action":"insert","lines":["t"]},{"start":{"row":97,"column":28},"end":{"row":97,"column":29},"action":"insert","lines":["e"]},{"start":{"row":97,"column":29},"end":{"row":97,"column":30},"action":"insert","lines":["r"]},{"start":{"row":97,"column":30},"end":{"row":97,"column":31},"action":"insert","lines":["m"]},{"start":{"row":97,"column":31},"end":{"row":97,"column":32},"action":"insert","lines":["_"]},{"start":{"row":97,"column":32},"end":{"row":97,"column":33},"action":"insert","lines":["n"]},{"start":{"row":97,"column":33},"end":{"row":97,"column":34},"action":"insert","lines":["a"]},{"start":{"row":97,"column":34},"end":{"row":97,"column":35},"action":"insert","lines":["m"]},{"start":{"row":97,"column":35},"end":{"row":97,"column":36},"action":"insert","lines":["e"]}],[{"start":{"row":93,"column":22},"end":{"row":93,"column":23},"action":"insert","lines":["/"],"id":146},{"start":{"row":93,"column":23},"end":{"row":93,"column":24},"action":"insert","lines":["<"]},{"start":{"row":93,"column":24},"end":{"row":93,"column":25},"action":"insert","lines":["t"]},{"start":{"row":93,"column":25},"end":{"row":93,"column":26},"action":"insert","lines":["e"]},{"start":{"row":93,"column":26},"end":{"row":93,"column":27},"action":"insert","lines":["r"]},{"start":{"row":93,"column":27},"end":{"row":93,"column":28},"action":"insert","lines":["m"]},{"start":{"row":93,"column":28},"end":{"row":93,"column":29},"action":"insert","lines":["_"]},{"start":{"row":93,"column":29},"end":{"row":93,"column":30},"action":"insert","lines":["n"]},{"start":{"row":93,"column":30},"end":{"row":93,"column":31},"action":"insert","lines":["a"]},{"start":{"row":93,"column":31},"end":{"row":93,"column":32},"action":"insert","lines":["m"]},{"start":{"row":93,"column":32},"end":{"row":93,"column":33},"action":"insert","lines":["e"]},{"start":{"row":93,"column":33},"end":{"row":93,"column":34},"action":"insert","lines":[">"]}],[{"start":{"row":96,"column":4},"end":{"row":96,"column":8},"action":"remove","lines":["term"],"id":147},{"start":{"row":96,"column":4},"end":{"row":96,"column":5},"action":"insert","lines":["r"]},{"start":{"row":96,"column":5},"end":{"row":96,"column":6},"action":"insert","lines":["e"]},{"start":{"row":96,"column":6},"end":{"row":96,"column":7},"action":"insert","lines":["s"]},{"start":{"row":96,"column":7},"end":{"row":96,"column":8},"action":"insert","lines":["t"]},{"start":{"row":96,"column":8},"end":{"row":96,"column":9},"action":"insert","lines":["u"]},{"start":{"row":96,"column":9},"end":{"row":96,"column":10},"action":"insert","lines":["l"]},{"start":{"row":96,"column":10},"end":{"row":96,"column":11},"action":"insert","lines":["t"]},{"start":{"row":96,"column":11},"end":{"row":96,"column":12},"action":"insert","lines":["s"]}],[{"start":{"row":96,"column":11},"end":{"row":96,"column":12},"action":"remove","lines":["s"],"id":148},{"start":{"row":96,"column":10},"end":{"row":96,"column":11},"action":"remove","lines":["t"]},{"start":{"row":96,"column":9},"end":{"row":96,"column":10},"action":"remove","lines":["l"]},{"start":{"row":96,"column":8},"end":{"row":96,"column":9},"action":"remove","lines":["u"]},{"start":{"row":96,"column":7},"end":{"row":96,"column":8},"action":"remove","lines":["t"]}],[{"start":{"row":96,"column":7},"end":{"row":96,"column":8},"action":"insert","lines":["u"],"id":149},{"start":{"row":96,"column":8},"end":{"row":96,"column":9},"action":"insert","lines":["l"]},{"start":{"row":96,"column":9},"end":{"row":96,"column":10},"action":"insert","lines":["t"]},{"start":{"row":96,"column":10},"end":{"row":96,"column":11},"action":"insert","lines":["s"]}],[{"start":{"row":93,"column":22},"end":{"row":93,"column":34},"action":"remove","lines":["/<term_name>"],"id":150}],[{"start":{"row":94,"column":14},"end":{"row":94,"column":23},"action":"remove","lines":["term_name"],"id":151}],[{"start":{"row":95,"column":4},"end":{"row":97,"column":40},"action":"remove","lines":["return render_template('searchresults.html',","    results=mongo.db.categories.find_one(","    {'term_name': ObjectId(term_name)}))"],"id":152}],[{"start":{"row":95,"column":4},"end":{"row":95,"column":47},"action":"insert","lines":["db.messages.createIndex({\"subject\":\"text\"})"],"id":153}],[{"start":{"row":95,"column":4},"end":{"row":95,"column":5},"action":"insert","lines":["s"],"id":154},{"start":{"row":95,"column":5},"end":{"row":95,"column":6},"action":"insert","lines":["e"]},{"start":{"row":95,"column":6},"end":{"row":95,"column":7},"action":"insert","lines":["a"]},{"start":{"row":95,"column":7},"end":{"row":95,"column":8},"action":"insert","lines":["r"]},{"start":{"row":95,"column":8},"end":{"row":95,"column":9},"action":"insert","lines":["c"]},{"start":{"row":95,"column":9},"end":{"row":95,"column":10},"action":"insert","lines":["h"]},{"start":{"row":95,"column":10},"end":{"row":95,"column":11},"action":"insert","lines":["_"]},{"start":{"row":95,"column":11},"end":{"row":95,"column":12},"action":"insert","lines":["r"]},{"start":{"row":95,"column":12},"end":{"row":95,"column":13},"action":"insert","lines":["e"]},{"start":{"row":95,"column":13},"end":{"row":95,"column":14},"action":"insert","lines":["s"]}],[{"start":{"row":95,"column":14},"end":{"row":95,"column":15},"action":"insert","lines":["u"],"id":155},{"start":{"row":95,"column":15},"end":{"row":95,"column":16},"action":"insert","lines":["l"]},{"start":{"row":95,"column":16},"end":{"row":95,"column":17},"action":"insert","lines":["t"]}],[{"start":{"row":95,"column":17},"end":{"row":95,"column":18},"action":"insert","lines":[" "],"id":156},{"start":{"row":95,"column":18},"end":{"row":95,"column":19},"action":"insert","lines":["="]}],[{"start":{"row":95,"column":19},"end":{"row":95,"column":20},"action":"insert","lines":[" "],"id":157}],[{"start":{"row":95,"column":23},"end":{"row":95,"column":31},"action":"remove","lines":["messages"],"id":158},{"start":{"row":95,"column":23},"end":{"row":95,"column":24},"action":"insert","lines":["t"]},{"start":{"row":95,"column":24},"end":{"row":95,"column":25},"action":"insert","lines":["e"]},{"start":{"row":95,"column":25},"end":{"row":95,"column":26},"action":"insert","lines":["r"]},{"start":{"row":95,"column":26},"end":{"row":95,"column":27},"action":"insert","lines":["m"]},{"start":{"row":95,"column":27},"end":{"row":95,"column":28},"action":"insert","lines":["s"]}],[{"start":{"row":95,"column":43},"end":{"row":95,"column":50},"action":"remove","lines":["subject"],"id":159},{"start":{"row":95,"column":43},"end":{"row":95,"column":44},"action":"insert","lines":["t"]},{"start":{"row":95,"column":44},"end":{"row":95,"column":45},"action":"insert","lines":["e"]},{"start":{"row":95,"column":45},"end":{"row":95,"column":46},"action":"insert","lines":["r"]},{"start":{"row":95,"column":46},"end":{"row":95,"column":47},"action":"insert","lines":["m"]}],[{"start":{"row":95,"column":43},"end":{"row":95,"column":47},"action":"remove","lines":["term"],"id":160},{"start":{"row":95,"column":43},"end":{"row":95,"column":52},"action":"insert","lines":["term_name"]}],[{"start":{"row":95,"column":55},"end":{"row":95,"column":59},"action":"remove","lines":["text"],"id":161},{"start":{"row":95,"column":55},"end":{"row":95,"column":56},"action":"insert","lines":["t"]},{"start":{"row":95,"column":56},"end":{"row":95,"column":57},"action":"insert","lines":["e"]},{"start":{"row":95,"column":57},"end":{"row":95,"column":58},"action":"insert","lines":["r"]},{"start":{"row":95,"column":58},"end":{"row":95,"column":59},"action":"insert","lines":["m"]}],[{"start":{"row":95,"column":62},"end":{"row":96,"column":0},"action":"insert","lines":["",""],"id":162},{"start":{"row":96,"column":0},"end":{"row":96,"column":4},"action":"insert","lines":["    "]},{"start":{"row":96,"column":4},"end":{"row":96,"column":5},"action":"insert","lines":["p"]},{"start":{"row":96,"column":5},"end":{"row":96,"column":6},"action":"insert","lines":["r"]},{"start":{"row":96,"column":6},"end":{"row":96,"column":7},"action":"insert","lines":["i"]},{"start":{"row":96,"column":7},"end":{"row":96,"column":8},"action":"insert","lines":["n"]},{"start":{"row":96,"column":8},"end":{"row":96,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":96,"column":9},"end":{"row":96,"column":11},"action":"insert","lines":["()"],"id":163}],[{"start":{"row":96,"column":10},"end":{"row":96,"column":11},"action":"insert","lines":["s"],"id":164},{"start":{"row":96,"column":11},"end":{"row":96,"column":12},"action":"insert","lines":["e"]},{"start":{"row":96,"column":12},"end":{"row":96,"column":13},"action":"insert","lines":["a"]},{"start":{"row":96,"column":13},"end":{"row":96,"column":14},"action":"insert","lines":["r"]}],[{"start":{"row":96,"column":10},"end":{"row":96,"column":14},"action":"remove","lines":["sear"],"id":165},{"start":{"row":96,"column":10},"end":{"row":96,"column":23},"action":"insert","lines":["search_result"]}],[{"start":{"row":94,"column":4},"end":{"row":94,"column":13},"action":"remove","lines":["find_term"],"id":166},{"start":{"row":94,"column":4},"end":{"row":94,"column":5},"action":"insert","lines":["s"]},{"start":{"row":94,"column":5},"end":{"row":94,"column":6},"action":"insert","lines":["e"]},{"start":{"row":94,"column":6},"end":{"row":94,"column":7},"action":"insert","lines":["a"]},{"start":{"row":94,"column":7},"end":{"row":94,"column":8},"action":"insert","lines":["r"]},{"start":{"row":94,"column":8},"end":{"row":94,"column":9},"action":"insert","lines":["c"]},{"start":{"row":94,"column":9},"end":{"row":94,"column":10},"action":"insert","lines":["h"]}],[{"start":{"row":93,"column":13},"end":{"row":93,"column":22},"action":"remove","lines":["find_term"],"id":167},{"start":{"row":93,"column":13},"end":{"row":93,"column":14},"action":"insert","lines":["s"]},{"start":{"row":93,"column":14},"end":{"row":93,"column":15},"action":"insert","lines":["e"]},{"start":{"row":93,"column":15},"end":{"row":93,"column":16},"action":"insert","lines":["a"]},{"start":{"row":93,"column":16},"end":{"row":93,"column":17},"action":"insert","lines":["r"]},{"start":{"row":93,"column":17},"end":{"row":93,"column":18},"action":"insert","lines":["c"]},{"start":{"row":93,"column":18},"end":{"row":93,"column":19},"action":"insert","lines":["h"]}],[{"start":{"row":94,"column":11},"end":{"row":94,"column":12},"action":"insert","lines":["t"],"id":168},{"start":{"row":94,"column":12},"end":{"row":94,"column":13},"action":"insert","lines":["e"]},{"start":{"row":94,"column":13},"end":{"row":94,"column":14},"action":"insert","lines":["r"]},{"start":{"row":94,"column":14},"end":{"row":94,"column":15},"action":"insert","lines":["m"]},{"start":{"row":94,"column":15},"end":{"row":94,"column":16},"action":"insert","lines":["s"]}],[{"start":{"row":95,"column":4},"end":{"row":95,"column":17},"action":"remove","lines":["search_result"],"id":169},{"start":{"row":95,"column":4},"end":{"row":95,"column":5},"action":"insert","lines":["t"]},{"start":{"row":95,"column":5},"end":{"row":95,"column":6},"action":"insert","lines":["e"]},{"start":{"row":95,"column":6},"end":{"row":95,"column":7},"action":"insert","lines":["r"]},{"start":{"row":95,"column":7},"end":{"row":95,"column":8},"action":"insert","lines":["m"]},{"start":{"row":95,"column":8},"end":{"row":95,"column":9},"action":"insert","lines":["s"]}],[{"start":{"row":96,"column":1},"end":{"row":96,"column":24},"action":"remove","lines":["   print(search_result)"],"id":170},{"start":{"row":96,"column":0},"end":{"row":96,"column":1},"action":"remove","lines":[" "]},{"start":{"row":95,"column":54},"end":{"row":96,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":95,"column":21},"end":{"row":95,"column":32},"action":"remove","lines":["createIndex"],"id":171},{"start":{"row":95,"column":21},"end":{"row":95,"column":22},"action":"insert","lines":["f"]},{"start":{"row":95,"column":22},"end":{"row":95,"column":23},"action":"insert","lines":["i"]},{"start":{"row":95,"column":23},"end":{"row":95,"column":24},"action":"insert","lines":["n"]},{"start":{"row":95,"column":24},"end":{"row":95,"column":25},"action":"insert","lines":["d"]}],[{"start":{"row":95,"column":27},"end":{"row":95,"column":28},"action":"remove","lines":["\""],"id":172}],[{"start":{"row":95,"column":27},"end":{"row":95,"column":28},"action":"insert","lines":["'"],"id":173}],[{"start":{"row":95,"column":38},"end":{"row":95,"column":39},"action":"remove","lines":[":"],"id":174}],[{"start":{"row":95,"column":38},"end":{"row":95,"column":39},"action":"insert","lines":["'"],"id":175}],[{"start":{"row":95,"column":38},"end":{"row":95,"column":45},"action":"remove","lines":["'\"term\""],"id":177},{"start":{"row":95,"column":37},"end":{"row":95,"column":38},"action":"remove","lines":["\""]}],[{"start":{"row":95,"column":37},"end":{"row":95,"column":38},"action":"insert","lines":["'"],"id":178},{"start":{"row":95,"column":38},"end":{"row":95,"column":39},"action":"insert","lines":[":"]}],[{"start":{"row":95,"column":39},"end":{"row":95,"column":40},"action":"insert","lines":[" "],"id":179}],[{"start":{"row":95,"column":40},"end":{"row":95,"column":73},"action":"insert","lines":["request.form.get('category_name')"],"id":180}],[{"start":{"row":95,"column":58},"end":{"row":95,"column":66},"action":"remove","lines":["category"],"id":181},{"start":{"row":95,"column":58},"end":{"row":95,"column":59},"action":"insert","lines":["t"]},{"start":{"row":95,"column":59},"end":{"row":95,"column":60},"action":"insert","lines":["e"]},{"start":{"row":95,"column":60},"end":{"row":95,"column":61},"action":"insert","lines":["r"]},{"start":{"row":95,"column":61},"end":{"row":95,"column":62},"action":"insert","lines":["m"]}],[{"start":{"row":95,"column":12},"end":{"row":95,"column":13},"action":"insert","lines":["m"],"id":182},{"start":{"row":95,"column":13},"end":{"row":95,"column":14},"action":"insert","lines":["o"]},{"start":{"row":95,"column":14},"end":{"row":95,"column":15},"action":"insert","lines":["n"]},{"start":{"row":95,"column":15},"end":{"row":95,"column":16},"action":"insert","lines":["g"]},{"start":{"row":95,"column":16},"end":{"row":95,"column":17},"action":"insert","lines":["o"]},{"start":{"row":95,"column":17},"end":{"row":95,"column":18},"action":"insert","lines":["."]}],[{"start":{"row":95,"column":77},"end":{"row":96,"column":0},"action":"insert","lines":["",""],"id":183},{"start":{"row":96,"column":0},"end":{"row":96,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":96,"column":4},"end":{"row":96,"column":5},"action":"insert","lines":["p"],"id":184},{"start":{"row":96,"column":5},"end":{"row":96,"column":6},"action":"insert","lines":["r"]},{"start":{"row":96,"column":6},"end":{"row":96,"column":7},"action":"insert","lines":["i"]},{"start":{"row":96,"column":7},"end":{"row":96,"column":8},"action":"insert","lines":["n"]},{"start":{"row":96,"column":8},"end":{"row":96,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":96,"column":9},"end":{"row":96,"column":11},"action":"insert","lines":["()"],"id":185}],[{"start":{"row":96,"column":10},"end":{"row":96,"column":11},"action":"insert","lines":["T"],"id":186},{"start":{"row":96,"column":11},"end":{"row":96,"column":12},"action":"insert","lines":["e"]},{"start":{"row":96,"column":12},"end":{"row":96,"column":13},"action":"insert","lines":["r"]},{"start":{"row":96,"column":13},"end":{"row":96,"column":14},"action":"insert","lines":["m"]},{"start":{"row":96,"column":14},"end":{"row":96,"column":15},"action":"insert","lines":["s"]}],[{"start":{"row":96,"column":14},"end":{"row":96,"column":15},"action":"remove","lines":["s"],"id":187},{"start":{"row":96,"column":13},"end":{"row":96,"column":14},"action":"remove","lines":["m"]},{"start":{"row":96,"column":12},"end":{"row":96,"column":13},"action":"remove","lines":["r"]},{"start":{"row":96,"column":11},"end":{"row":96,"column":12},"action":"remove","lines":["e"]},{"start":{"row":96,"column":10},"end":{"row":96,"column":11},"action":"remove","lines":["T"]}],[{"start":{"row":96,"column":10},"end":{"row":96,"column":11},"action":"insert","lines":["t"],"id":188},{"start":{"row":96,"column":11},"end":{"row":96,"column":12},"action":"insert","lines":["e"]},{"start":{"row":96,"column":12},"end":{"row":96,"column":13},"action":"insert","lines":["r"]},{"start":{"row":96,"column":13},"end":{"row":96,"column":14},"action":"insert","lines":["m"]},{"start":{"row":96,"column":14},"end":{"row":96,"column":15},"action":"insert","lines":["s"]}],[{"start":{"row":93,"column":0},"end":{"row":96,"column":16},"action":"remove","lines":["@app.route('/search', methods=['POST'])","def search(terms):","    terms = mongo.db.terms.find({'term_name': request.form.get('term_name')})","    print(terms)"],"id":189},{"start":{"row":93,"column":0},"end":{"row":99,"column":58},"action":"insert","lines":["@app.route('/search')","def search():","    \"\"\"Route for search bar\"\"\"","    db_query = request.args['db_query']","    results = mongo.db.recipe.find({'$text': {'$search': db_query }}).sort('_id', pymongo.ASCENDING)","​","    return render_template('search.html', results=results)"]}],[{"start":{"row":98,"column":0},"end":{"row":98,"column":1},"action":"remove","lines":["​"],"id":190}],[{"start":{"row":97,"column":23},"end":{"row":97,"column":29},"action":"remove","lines":["recipe"],"id":191},{"start":{"row":97,"column":23},"end":{"row":97,"column":24},"action":"insert","lines":["t"]},{"start":{"row":97,"column":24},"end":{"row":97,"column":25},"action":"insert","lines":["e"]},{"start":{"row":97,"column":25},"end":{"row":97,"column":26},"action":"insert","lines":["r"]},{"start":{"row":97,"column":26},"end":{"row":97,"column":27},"action":"insert","lines":["m"]},{"start":{"row":97,"column":27},"end":{"row":97,"column":28},"action":"insert","lines":["s"]}],[{"start":{"row":97,"column":69},"end":{"row":97,"column":99},"action":"remove","lines":["sort('_id', pymongo.ASCENDING)"],"id":192},{"start":{"row":97,"column":68},"end":{"row":97,"column":69},"action":"remove","lines":["."]}],[{"start":{"row":97,"column":68},"end":{"row":98,"column":0},"action":"remove","lines":["",""],"id":193}],[{"start":{"row":97,"column":4},"end":{"row":97,"column":14},"action":"remove","lines":["results = "],"id":198}],[{"start":{"row":96,"column":5},"end":{"row":96,"column":39},"action":"remove","lines":["b_query = request.args['db_query']"],"id":199},{"start":{"row":96,"column":4},"end":{"row":96,"column":5},"action":"remove","lines":["d"]},{"start":{"row":96,"column":0},"end":{"row":96,"column":4},"action":"remove","lines":["    "]},{"start":{"row":95,"column":30},"end":{"row":96,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":95,"column":30},"end":{"row":96,"column":0},"action":"insert","lines":["",""],"id":200},{"start":{"row":96,"column":0},"end":{"row":96,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":96,"column":4},"end":{"row":96,"column":72},"action":"insert","lines":["category_doc = {'category_name': request.form.get('category_name')},"],"id":201}],[{"start":{"row":96,"column":4},"end":{"row":96,"column":16},"action":"remove","lines":["category_doc"],"id":202},{"start":{"row":96,"column":4},"end":{"row":96,"column":5},"action":"insert","lines":["s"]},{"start":{"row":96,"column":5},"end":{"row":96,"column":6},"action":"insert","lines":["e"]},{"start":{"row":96,"column":6},"end":{"row":96,"column":7},"action":"insert","lines":["a"]},{"start":{"row":96,"column":7},"end":{"row":96,"column":8},"action":"insert","lines":["r"]},{"start":{"row":96,"column":8},"end":{"row":96,"column":9},"action":"insert","lines":["c"]},{"start":{"row":96,"column":9},"end":{"row":96,"column":10},"action":"insert","lines":["h"]}],[{"start":{"row":96,"column":10},"end":{"row":96,"column":11},"action":"insert","lines":["_"],"id":203},{"start":{"row":96,"column":11},"end":{"row":96,"column":12},"action":"insert","lines":["t"]},{"start":{"row":96,"column":12},"end":{"row":96,"column":13},"action":"insert","lines":["e"]},{"start":{"row":96,"column":13},"end":{"row":96,"column":14},"action":"insert","lines":["r"]},{"start":{"row":96,"column":14},"end":{"row":96,"column":15},"action":"insert","lines":["m"]}],[{"start":{"row":96,"column":20},"end":{"row":96,"column":27},"action":"remove","lines":["categor"],"id":204}],[{"start":{"row":96,"column":20},"end":{"row":96,"column":21},"action":"remove","lines":["y"],"id":205}],[{"start":{"row":96,"column":20},"end":{"row":96,"column":21},"action":"insert","lines":["t"],"id":206},{"start":{"row":96,"column":21},"end":{"row":96,"column":22},"action":"insert","lines":["e"]},{"start":{"row":96,"column":22},"end":{"row":96,"column":23},"action":"insert","lines":["r"]},{"start":{"row":96,"column":23},"end":{"row":96,"column":24},"action":"insert","lines":["m"]}],[{"start":{"row":96,"column":50},"end":{"row":96,"column":58},"action":"remove","lines":["category"],"id":207},{"start":{"row":96,"column":50},"end":{"row":96,"column":51},"action":"insert","lines":["t"]},{"start":{"row":96,"column":51},"end":{"row":96,"column":52},"action":"insert","lines":["e"]},{"start":{"row":96,"column":52},"end":{"row":96,"column":53},"action":"insert","lines":["r"]},{"start":{"row":96,"column":53},"end":{"row":96,"column":54},"action":"insert","lines":["m"]}],[{"start":{"row":97,"column":45},"end":{"row":97,"column":54},"action":"remove","lines":[" db_query"],"id":208},{"start":{"row":97,"column":45},"end":{"row":97,"column":46},"action":"insert","lines":[" "]},{"start":{"row":97,"column":46},"end":{"row":97,"column":47},"action":"insert","lines":["s"]},{"start":{"row":97,"column":47},"end":{"row":97,"column":48},"action":"insert","lines":["e"]},{"start":{"row":97,"column":48},"end":{"row":97,"column":49},"action":"insert","lines":["a"]},{"start":{"row":97,"column":49},"end":{"row":97,"column":50},"action":"insert","lines":["r"]},{"start":{"row":97,"column":50},"end":{"row":97,"column":51},"action":"insert","lines":["c"]}],[{"start":{"row":97,"column":46},"end":{"row":97,"column":51},"action":"remove","lines":["searc"],"id":209},{"start":{"row":97,"column":46},"end":{"row":97,"column":57},"action":"insert","lines":["search_term"]}],[{"start":{"row":97,"column":45},"end":{"row":97,"column":46},"action":"remove","lines":[" "],"id":210}],[{"start":{"row":97,"column":45},"end":{"row":97,"column":46},"action":"insert","lines":[" "],"id":211}],[{"start":{"row":98,"column":42},"end":{"row":98,"column":57},"action":"remove","lines":["results=results"],"id":212},{"start":{"row":98,"column":42},"end":{"row":98,"column":43},"action":"insert","lines":["s"]},{"start":{"row":98,"column":43},"end":{"row":98,"column":44},"action":"insert","lines":["e"]},{"start":{"row":98,"column":44},"end":{"row":98,"column":45},"action":"insert","lines":["a"]},{"start":{"row":98,"column":45},"end":{"row":98,"column":46},"action":"insert","lines":["r"]},{"start":{"row":98,"column":46},"end":{"row":98,"column":47},"action":"insert","lines":["c"]},{"start":{"row":98,"column":47},"end":{"row":98,"column":48},"action":"insert","lines":["h"]}],[{"start":{"row":98,"column":42},"end":{"row":98,"column":48},"action":"remove","lines":["search"],"id":213},{"start":{"row":98,"column":42},"end":{"row":98,"column":53},"action":"insert","lines":["search_term"]}],[{"start":{"row":98,"column":53},"end":{"row":98,"column":54},"action":"insert","lines":["="],"id":214},{"start":{"row":98,"column":54},"end":{"row":98,"column":55},"action":"insert","lines":["s"]},{"start":{"row":98,"column":55},"end":{"row":98,"column":56},"action":"insert","lines":["e"]},{"start":{"row":98,"column":56},"end":{"row":98,"column":57},"action":"insert","lines":["a"]},{"start":{"row":98,"column":57},"end":{"row":98,"column":58},"action":"insert","lines":["r"]},{"start":{"row":98,"column":58},"end":{"row":98,"column":59},"action":"insert","lines":["c"]}],[{"start":{"row":98,"column":54},"end":{"row":98,"column":59},"action":"remove","lines":["searc"],"id":215},{"start":{"row":98,"column":54},"end":{"row":98,"column":65},"action":"insert","lines":["search_term"]}],[{"start":{"row":93,"column":0},"end":{"row":98,"column":66},"action":"remove","lines":["@app.route('/search')","def search():","    \"\"\"Route for search bar\"\"\"","    search_term = {'term_name': request.form.get('term_name')},","    mongo.db.terms.find({'$text': {'$search': search_term }})","    return render_template('search.html', search_term=search_term)"],"id":216},{"start":{"row":93,"column":0},"end":{"row":99,"column":58},"action":"insert","lines":["@app.route('/search')","def search():","    \"\"\"Route for search bar\"\"\"","    db_query = request.args['db_query']","    results = mongo.db.recipe.find({'$text': {'$search': db_query }}).sort('_id', pymongo.ASCENDING)","​","    return render_template('search.html', results=results)"]}],[{"start":{"row":98,"column":0},"end":{"row":98,"column":1},"action":"remove","lines":["​"],"id":217},{"start":{"row":97,"column":100},"end":{"row":98,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":97,"column":70},"end":{"row":97,"column":100},"action":"remove","lines":["sort('_id', pymongo.ASCENDING)"],"id":218},{"start":{"row":97,"column":69},"end":{"row":97,"column":70},"action":"remove","lines":["."]}],[{"start":{"row":96,"column":4},"end":{"row":96,"column":12},"action":"remove","lines":["db_query"],"id":219},{"start":{"row":96,"column":4},"end":{"row":96,"column":5},"action":"insert","lines":["t"]},{"start":{"row":96,"column":5},"end":{"row":96,"column":6},"action":"insert","lines":["e"]},{"start":{"row":96,"column":6},"end":{"row":96,"column":7},"action":"insert","lines":["r"]}],[{"start":{"row":96,"column":7},"end":{"row":96,"column":8},"action":"insert","lines":["m"],"id":220}],[{"start":{"row":96,"column":8},"end":{"row":96,"column":9},"action":"insert","lines":["s"],"id":221}],[{"start":{"row":96,"column":26},"end":{"row":96,"column":34},"action":"remove","lines":["db_query"],"id":222},{"start":{"row":96,"column":26},"end":{"row":96,"column":27},"action":"insert","lines":["t"]},{"start":{"row":96,"column":27},"end":{"row":96,"column":28},"action":"insert","lines":["e"]},{"start":{"row":96,"column":28},"end":{"row":96,"column":29},"action":"insert","lines":["r"]},{"start":{"row":96,"column":29},"end":{"row":96,"column":30},"action":"insert","lines":["m"]},{"start":{"row":96,"column":30},"end":{"row":96,"column":31},"action":"insert","lines":["s"]}],[{"start":{"row":97,"column":57},"end":{"row":97,"column":65},"action":"remove","lines":["db_query"],"id":223},{"start":{"row":97,"column":57},"end":{"row":97,"column":58},"action":"insert","lines":["t"]},{"start":{"row":97,"column":58},"end":{"row":97,"column":59},"action":"insert","lines":["e"]},{"start":{"row":97,"column":59},"end":{"row":97,"column":60},"action":"insert","lines":["r"]},{"start":{"row":97,"column":60},"end":{"row":97,"column":61},"action":"insert","lines":["m"]},{"start":{"row":97,"column":61},"end":{"row":97,"column":62},"action":"insert","lines":["s"]}],[{"start":{"row":96,"column":30},"end":{"row":96,"column":31},"action":"remove","lines":["s"],"id":224}],[{"start":{"row":96,"column":30},"end":{"row":96,"column":31},"action":"insert","lines":["_"],"id":225},{"start":{"row":96,"column":31},"end":{"row":96,"column":32},"action":"insert","lines":["n"]},{"start":{"row":96,"column":32},"end":{"row":96,"column":33},"action":"insert","lines":["a"]},{"start":{"row":96,"column":33},"end":{"row":96,"column":34},"action":"insert","lines":["m"]},{"start":{"row":96,"column":34},"end":{"row":96,"column":35},"action":"insert","lines":["e"]}],[{"start":{"row":96,"column":8},"end":{"row":96,"column":9},"action":"remove","lines":["s"],"id":226}],[{"start":{"row":96,"column":8},"end":{"row":96,"column":9},"action":"insert","lines":["_"],"id":227},{"start":{"row":96,"column":9},"end":{"row":96,"column":10},"action":"insert","lines":["n"]},{"start":{"row":96,"column":10},"end":{"row":96,"column":11},"action":"insert","lines":["a"]},{"start":{"row":96,"column":11},"end":{"row":96,"column":12},"action":"insert","lines":["m"]},{"start":{"row":96,"column":12},"end":{"row":96,"column":13},"action":"insert","lines":["e"]}],[{"start":{"row":97,"column":61},"end":{"row":97,"column":62},"action":"remove","lines":["s"],"id":228}],[{"start":{"row":97,"column":61},"end":{"row":97,"column":62},"action":"insert","lines":["_"],"id":229},{"start":{"row":97,"column":62},"end":{"row":97,"column":63},"action":"insert","lines":["n"]},{"start":{"row":97,"column":63},"end":{"row":97,"column":64},"action":"insert","lines":["a"]},{"start":{"row":97,"column":64},"end":{"row":97,"column":65},"action":"insert","lines":["m"]},{"start":{"row":97,"column":65},"end":{"row":97,"column":66},"action":"insert","lines":["e"]}],[{"start":{"row":93,"column":20},"end":{"row":93,"column":21},"action":"insert","lines":[","],"id":230}],[{"start":{"row":93,"column":21},"end":{"row":93,"column":22},"action":"insert","lines":[" "],"id":231}],[{"start":{"row":93,"column":22},"end":{"row":93,"column":40},"action":"insert","lines":[", methods=['POST']"],"id":232}],[{"start":{"row":93,"column":23},"end":{"row":93,"column":24},"action":"remove","lines":[" "],"id":233},{"start":{"row":93,"column":22},"end":{"row":93,"column":23},"action":"remove","lines":[","]}],[{"start":{"row":93,"column":20},"end":{"row":93,"column":38},"action":"remove","lines":[", methods=['POST']"],"id":234}],[{"start":{"row":96,"column":28},"end":{"row":96,"column":41},"action":"remove","lines":["['term_name']"],"id":235},{"start":{"row":96,"column":28},"end":{"row":96,"column":53},"action":"insert","lines":["form.get('category_name')"]}],[{"start":{"row":96,"column":24},"end":{"row":96,"column":28},"action":"remove","lines":["args"],"id":236}],[{"start":{"row":96,"column":34},"end":{"row":96,"column":41},"action":"remove","lines":["categor"],"id":237}],[{"start":{"row":96,"column":34},"end":{"row":96,"column":35},"action":"insert","lines":["t"],"id":238},{"start":{"row":96,"column":35},"end":{"row":96,"column":36},"action":"insert","lines":["e"]},{"start":{"row":96,"column":36},"end":{"row":96,"column":37},"action":"insert","lines":["r"]},{"start":{"row":96,"column":37},"end":{"row":96,"column":38},"action":"insert","lines":["m"]}],[{"start":{"row":96,"column":38},"end":{"row":96,"column":39},"action":"remove","lines":["y"],"id":239}]]},"ace":{"folds":[],"scrolltop":1066,"scrollleft":0,"selection":{"start":{"row":94,"column":13},"end":{"row":94,"column":13},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":65,"state":"start","mode":"ace/mode/python"}},"timestamp":1565291271954,"hash":"c6f3128536b76f196b1b6d2814c26cd3657481b0"}