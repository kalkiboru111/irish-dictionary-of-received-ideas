{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":101,"column":0},"end":{"row":118,"column":41},"action":"insert","lines":["@app.route('/find_recipes', methods=['GET', 'POST'])","def find_recipes():","    if request.method=='POST':","        ","        # get the search term","        search_term = request.form.get(\"search_term\")","        ","        #  create the index","        mongo.db.recipes.create_index( [(\"$**\", 'text')] )","        ","         # search with the search term that came through the form","        cursor = mongo.db.recipes.find({ \"$text\": { \"$search\": search_term } })","        recipes = [recipe for recipe in cursor]","        ","        # send recipes to page","        return render_template('search.html', recipes=recipes, query=search_term)","        ","    return render_template('search.html')"],"id":1128}],[{"start":{"row":91,"column":0},"end":{"row":91,"column":1},"action":"insert","lines":["#"],"id":1129}],[{"start":{"row":91,"column":1},"end":{"row":91,"column":2},"action":"insert","lines":[" "],"id":1130}],[{"start":{"row":91,"column":1},"end":{"row":91,"column":2},"action":"remove","lines":[" "],"id":1131},{"start":{"row":91,"column":0},"end":{"row":91,"column":1},"action":"remove","lines":["#"]}],[{"start":{"row":91,"column":0},"end":{"row":91,"column":1},"action":"insert","lines":["'"],"id":1132},{"start":{"row":91,"column":1},"end":{"row":91,"column":2},"action":"insert","lines":["'"]},{"start":{"row":91,"column":2},"end":{"row":91,"column":3},"action":"insert","lines":["'"]}],[{"start":{"row":91,"column":3},"end":{"row":91,"column":4},"action":"insert","lines":[" "],"id":1133}],[{"start":{"row":99,"column":48},"end":{"row":100,"column":0},"action":"insert","lines":["",""],"id":1134},{"start":{"row":100,"column":0},"end":{"row":100,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":100,"column":0},"end":{"row":100,"column":4},"action":"remove","lines":["    "],"id":1135}],[{"start":{"row":100,"column":0},"end":{"row":100,"column":2},"action":"insert","lines":["''"],"id":1136}],[{"start":{"row":100,"column":2},"end":{"row":100,"column":3},"action":"insert","lines":["'"],"id":1137}],[{"start":{"row":102,"column":13},"end":{"row":102,"column":25},"action":"remove","lines":["find_recipes"],"id":1138},{"start":{"row":102,"column":13},"end":{"row":102,"column":14},"action":"insert","lines":["s"]},{"start":{"row":102,"column":14},"end":{"row":102,"column":15},"action":"insert","lines":["e"]},{"start":{"row":102,"column":15},"end":{"row":102,"column":16},"action":"insert","lines":["a"]},{"start":{"row":102,"column":16},"end":{"row":102,"column":17},"action":"insert","lines":["r"]},{"start":{"row":102,"column":17},"end":{"row":102,"column":18},"action":"insert","lines":["c"]},{"start":{"row":102,"column":18},"end":{"row":102,"column":19},"action":"insert","lines":["h"]}],[{"start":{"row":103,"column":4},"end":{"row":103,"column":16},"action":"remove","lines":["find_recipes"],"id":1139},{"start":{"row":103,"column":4},"end":{"row":103,"column":5},"action":"insert","lines":["s"]},{"start":{"row":103,"column":5},"end":{"row":103,"column":6},"action":"insert","lines":["e"]},{"start":{"row":103,"column":6},"end":{"row":103,"column":7},"action":"insert","lines":["a"]},{"start":{"row":103,"column":7},"end":{"row":103,"column":8},"action":"insert","lines":["r"]},{"start":{"row":103,"column":8},"end":{"row":103,"column":9},"action":"insert","lines":["c"]},{"start":{"row":103,"column":9},"end":{"row":103,"column":10},"action":"insert","lines":["h"]}],[{"start":{"row":103,"column":11},"end":{"row":103,"column":12},"action":"insert","lines":["s"],"id":1140},{"start":{"row":103,"column":12},"end":{"row":103,"column":13},"action":"insert","lines":["e"]},{"start":{"row":103,"column":13},"end":{"row":103,"column":14},"action":"insert","lines":["a"]},{"start":{"row":103,"column":14},"end":{"row":103,"column":15},"action":"insert","lines":["r"]},{"start":{"row":103,"column":15},"end":{"row":103,"column":16},"action":"insert","lines":["c"]}],[{"start":{"row":103,"column":11},"end":{"row":103,"column":16},"action":"remove","lines":["searc"],"id":1141},{"start":{"row":103,"column":11},"end":{"row":103,"column":22},"action":"insert","lines":["search_text"]}],[{"start":{"row":107,"column":17},"end":{"row":107,"column":18},"action":"remove","lines":["r"],"id":1142}],[{"start":{"row":107,"column":17},"end":{"row":107,"column":18},"action":"insert","lines":["s"],"id":1143}],[{"start":{"row":107,"column":18},"end":{"row":107,"column":19},"action":"remove","lines":["m"],"id":1144},{"start":{"row":107,"column":17},"end":{"row":107,"column":18},"action":"remove","lines":["s"]}],[{"start":{"row":107,"column":17},"end":{"row":107,"column":18},"action":"insert","lines":["x"],"id":1145},{"start":{"row":107,"column":18},"end":{"row":107,"column":19},"action":"insert","lines":["t"]}],[{"start":{"row":107,"column":47},"end":{"row":107,"column":51},"action":"remove","lines":["term"],"id":1146},{"start":{"row":107,"column":47},"end":{"row":107,"column":48},"action":"insert","lines":["t"]},{"start":{"row":107,"column":48},"end":{"row":107,"column":49},"action":"insert","lines":["e"]},{"start":{"row":107,"column":49},"end":{"row":107,"column":50},"action":"insert","lines":["x"]},{"start":{"row":107,"column":50},"end":{"row":107,"column":51},"action":"insert","lines":["t"]}],[{"start":{"row":110,"column":17},"end":{"row":110,"column":24},"action":"remove","lines":["recipes"],"id":1147},{"start":{"row":110,"column":17},"end":{"row":110,"column":18},"action":"insert","lines":["t"]},{"start":{"row":110,"column":18},"end":{"row":110,"column":19},"action":"insert","lines":["e"]},{"start":{"row":110,"column":19},"end":{"row":110,"column":20},"action":"insert","lines":["r"]},{"start":{"row":110,"column":20},"end":{"row":110,"column":21},"action":"insert","lines":["m"]},{"start":{"row":110,"column":21},"end":{"row":110,"column":22},"action":"insert","lines":["s"]}],[{"start":{"row":113,"column":26},"end":{"row":113,"column":33},"action":"remove","lines":["recipes"],"id":1148},{"start":{"row":113,"column":26},"end":{"row":113,"column":27},"action":"insert","lines":["t"]},{"start":{"row":113,"column":27},"end":{"row":113,"column":28},"action":"insert","lines":["e"]},{"start":{"row":113,"column":28},"end":{"row":113,"column":29},"action":"insert","lines":["r"]},{"start":{"row":113,"column":29},"end":{"row":113,"column":30},"action":"insert","lines":["m"]},{"start":{"row":113,"column":30},"end":{"row":113,"column":31},"action":"insert","lines":["s"]}],[{"start":{"row":113,"column":71},"end":{"row":113,"column":72},"action":"remove","lines":["m"],"id":1149},{"start":{"row":113,"column":70},"end":{"row":113,"column":71},"action":"remove","lines":["r"]}],[{"start":{"row":113,"column":70},"end":{"row":113,"column":71},"action":"insert","lines":["s"],"id":1150},{"start":{"row":113,"column":71},"end":{"row":113,"column":72},"action":"insert","lines":["t"]}],[{"start":{"row":113,"column":71},"end":{"row":113,"column":72},"action":"remove","lines":["t"],"id":1151},{"start":{"row":113,"column":70},"end":{"row":113,"column":71},"action":"remove","lines":["s"]}],[{"start":{"row":113,"column":70},"end":{"row":113,"column":71},"action":"insert","lines":["x"],"id":1152},{"start":{"row":113,"column":71},"end":{"row":113,"column":72},"action":"insert","lines":["t"]}],[{"start":{"row":114,"column":8},"end":{"row":114,"column":15},"action":"remove","lines":["recipes"],"id":1153},{"start":{"row":114,"column":8},"end":{"row":114,"column":9},"action":"insert","lines":["t"]},{"start":{"row":114,"column":9},"end":{"row":114,"column":10},"action":"insert","lines":["e"]},{"start":{"row":114,"column":10},"end":{"row":114,"column":11},"action":"insert","lines":["r"]},{"start":{"row":114,"column":11},"end":{"row":114,"column":12},"action":"insert","lines":["m"]},{"start":{"row":114,"column":12},"end":{"row":114,"column":13},"action":"insert","lines":["s"]}],[{"start":{"row":114,"column":17},"end":{"row":114,"column":23},"action":"remove","lines":["recipe"],"id":1154},{"start":{"row":114,"column":17},"end":{"row":114,"column":18},"action":"insert","lines":["t"]},{"start":{"row":114,"column":18},"end":{"row":114,"column":19},"action":"insert","lines":["e"]},{"start":{"row":114,"column":19},"end":{"row":114,"column":20},"action":"insert","lines":["r"]},{"start":{"row":114,"column":20},"end":{"row":114,"column":21},"action":"insert","lines":["m"]}],[{"start":{"row":114,"column":26},"end":{"row":114,"column":32},"action":"remove","lines":["recipe"],"id":1155},{"start":{"row":114,"column":26},"end":{"row":114,"column":27},"action":"insert","lines":["t"]},{"start":{"row":114,"column":27},"end":{"row":114,"column":28},"action":"insert","lines":["e"]},{"start":{"row":114,"column":28},"end":{"row":114,"column":29},"action":"insert","lines":["r"]},{"start":{"row":114,"column":29},"end":{"row":114,"column":30},"action":"insert","lines":["m"]},{"start":{"row":114,"column":30},"end":{"row":114,"column":31},"action":"insert","lines":["s"]}],[{"start":{"row":117,"column":46},"end":{"row":117,"column":61},"action":"remove","lines":["recipes=recipes"],"id":1156},{"start":{"row":117,"column":46},"end":{"row":117,"column":47},"action":"insert","lines":["t"]},{"start":{"row":117,"column":47},"end":{"row":117,"column":48},"action":"insert","lines":["e"]},{"start":{"row":117,"column":48},"end":{"row":117,"column":49},"action":"insert","lines":["r"]},{"start":{"row":117,"column":49},"end":{"row":117,"column":50},"action":"insert","lines":["m"]},{"start":{"row":117,"column":50},"end":{"row":117,"column":51},"action":"insert","lines":["s"]},{"start":{"row":117,"column":51},"end":{"row":117,"column":52},"action":"insert","lines":["="]}],[{"start":{"row":117,"column":52},"end":{"row":117,"column":53},"action":"insert","lines":["t"],"id":1157},{"start":{"row":117,"column":53},"end":{"row":117,"column":54},"action":"insert","lines":["e"]},{"start":{"row":117,"column":54},"end":{"row":117,"column":55},"action":"insert","lines":["r"]},{"start":{"row":117,"column":55},"end":{"row":117,"column":56},"action":"insert","lines":["m"]},{"start":{"row":117,"column":56},"end":{"row":117,"column":57},"action":"insert","lines":["s"]}],[{"start":{"row":117,"column":74},"end":{"row":117,"column":76},"action":"remove","lines":["rm"],"id":1158},{"start":{"row":117,"column":74},"end":{"row":117,"column":75},"action":"insert","lines":["x"]},{"start":{"row":117,"column":75},"end":{"row":117,"column":76},"action":"insert","lines":["t"]}],[{"start":{"row":114,"column":21},"end":{"row":114,"column":22},"action":"insert","lines":["s"],"id":1159}],[{"start":{"row":102,"column":19},"end":{"row":102,"column":20},"action":"insert","lines":["/"],"id":1160},{"start":{"row":102,"column":20},"end":{"row":102,"column":21},"action":"insert","lines":["<"]},{"start":{"row":102,"column":21},"end":{"row":102,"column":22},"action":"insert","lines":["s"]},{"start":{"row":102,"column":22},"end":{"row":102,"column":23},"action":"insert","lines":["e"]},{"start":{"row":102,"column":23},"end":{"row":102,"column":24},"action":"insert","lines":["a"]},{"start":{"row":102,"column":24},"end":{"row":102,"column":25},"action":"insert","lines":["r"]},{"start":{"row":102,"column":25},"end":{"row":102,"column":26},"action":"insert","lines":["c"]},{"start":{"row":102,"column":26},"end":{"row":102,"column":27},"action":"insert","lines":["h"]}],[{"start":{"row":102,"column":27},"end":{"row":102,"column":28},"action":"insert","lines":["_"],"id":1161},{"start":{"row":102,"column":28},"end":{"row":102,"column":29},"action":"insert","lines":["t"]},{"start":{"row":102,"column":29},"end":{"row":102,"column":30},"action":"insert","lines":["s"]},{"start":{"row":102,"column":30},"end":{"row":102,"column":31},"action":"insert","lines":["t"]}],[{"start":{"row":102,"column":30},"end":{"row":102,"column":31},"action":"remove","lines":["t"],"id":1162},{"start":{"row":102,"column":29},"end":{"row":102,"column":30},"action":"remove","lines":["s"]}],[{"start":{"row":102,"column":29},"end":{"row":102,"column":30},"action":"insert","lines":["e"],"id":1163},{"start":{"row":102,"column":30},"end":{"row":102,"column":31},"action":"insert","lines":["x"]},{"start":{"row":102,"column":31},"end":{"row":102,"column":32},"action":"insert","lines":["t"]},{"start":{"row":102,"column":32},"end":{"row":102,"column":33},"action":"insert","lines":[">"]}],[{"start":{"row":100,"column":0},"end":{"row":119,"column":41},"action":"remove","lines":["'''","","@app.route('/search/<search_text>', methods=['GET', 'POST'])","def search(search_text):","    if request.method=='POST':","        ","        # get the search term","        search_text = request.form.get(\"search_text\")","        ","        #  create the index","        mongo.db.terms.create_index( [(\"$**\", 'text')] )","        ","         # search with the search term that came through the form","        cursor = mongo.db.terms.find({ \"$text\": { \"$search\": search_text } })","        terms = [terms for terms in cursor]","        ","        # send recipes to page","        return render_template('search.html', terms=terms, query=search_text)","        ","    return render_template('search.html')"],"id":1164}],[{"start":{"row":91,"column":0},"end":{"row":91,"column":4},"action":"remove","lines":["''' "],"id":1165}],[{"start":{"row":99,"column":47},"end":{"row":99,"column":48},"action":"insert","lines":["_"],"id":1166},{"start":{"row":99,"column":48},"end":{"row":99,"column":49},"action":"insert","lines":["n"]},{"start":{"row":99,"column":49},"end":{"row":99,"column":50},"action":"insert","lines":["a"]},{"start":{"row":99,"column":50},"end":{"row":99,"column":51},"action":"insert","lines":["m"]},{"start":{"row":99,"column":51},"end":{"row":99,"column":52},"action":"insert","lines":["e"]},{"start":{"row":99,"column":52},"end":{"row":99,"column":53},"action":"insert","lines":["="]},{"start":{"row":99,"column":53},"end":{"row":99,"column":54},"action":"insert","lines":["t"]},{"start":{"row":99,"column":54},"end":{"row":99,"column":55},"action":"insert","lines":["e"]},{"start":{"row":99,"column":55},"end":{"row":99,"column":56},"action":"insert","lines":["r"]},{"start":{"row":99,"column":56},"end":{"row":99,"column":57},"action":"insert","lines":["m"]}],[{"start":{"row":99,"column":53},"end":{"row":99,"column":57},"action":"remove","lines":["term"],"id":1167},{"start":{"row":99,"column":53},"end":{"row":99,"column":62},"action":"insert","lines":["term_name"]}],[{"start":{"row":99,"column":62},"end":{"row":99,"column":63},"action":"insert","lines":[","],"id":1168}],[{"start":{"row":99,"column":63},"end":{"row":99,"column":64},"action":"insert","lines":[" "],"id":1169},{"start":{"row":99,"column":64},"end":{"row":99,"column":65},"action":"insert","lines":["r"]},{"start":{"row":99,"column":65},"end":{"row":99,"column":66},"action":"insert","lines":["e"]},{"start":{"row":99,"column":66},"end":{"row":99,"column":67},"action":"insert","lines":["s"]},{"start":{"row":99,"column":67},"end":{"row":99,"column":68},"action":"insert","lines":["u"]},{"start":{"row":99,"column":68},"end":{"row":99,"column":69},"action":"insert","lines":["l"]},{"start":{"row":99,"column":69},"end":{"row":99,"column":70},"action":"insert","lines":["t"]},{"start":{"row":99,"column":70},"end":{"row":99,"column":71},"action":"insert","lines":["s"]},{"start":{"row":99,"column":71},"end":{"row":99,"column":72},"action":"insert","lines":["="]},{"start":{"row":99,"column":72},"end":{"row":99,"column":73},"action":"insert","lines":["r"]}],[{"start":{"row":99,"column":73},"end":{"row":99,"column":74},"action":"insert","lines":["e"],"id":1170},{"start":{"row":99,"column":74},"end":{"row":99,"column":75},"action":"insert","lines":["s"]},{"start":{"row":99,"column":75},"end":{"row":99,"column":76},"action":"insert","lines":["u"]},{"start":{"row":99,"column":76},"end":{"row":99,"column":77},"action":"insert","lines":["l"]},{"start":{"row":99,"column":77},"end":{"row":99,"column":78},"action":"insert","lines":["t"]},{"start":{"row":99,"column":78},"end":{"row":99,"column":79},"action":"insert","lines":["s"]}],[{"start":{"row":99,"column":64},"end":{"row":99,"column":65},"action":"insert","lines":["t"],"id":1171},{"start":{"row":99,"column":65},"end":{"row":99,"column":66},"action":"insert","lines":["e"]},{"start":{"row":99,"column":66},"end":{"row":99,"column":67},"action":"insert","lines":["r"]},{"start":{"row":99,"column":67},"end":{"row":99,"column":68},"action":"insert","lines":["m"]},{"start":{"row":99,"column":68},"end":{"row":99,"column":69},"action":"insert","lines":["_"]},{"start":{"row":99,"column":69},"end":{"row":99,"column":70},"action":"insert","lines":["d"]},{"start":{"row":99,"column":70},"end":{"row":99,"column":71},"action":"insert","lines":["e"]},{"start":{"row":99,"column":71},"end":{"row":99,"column":72},"action":"insert","lines":["f"]},{"start":{"row":99,"column":72},"end":{"row":99,"column":73},"action":"insert","lines":["i"]},{"start":{"row":99,"column":73},"end":{"row":99,"column":74},"action":"insert","lines":["n"]},{"start":{"row":99,"column":74},"end":{"row":99,"column":75},"action":"insert","lines":["i"]}],[{"start":{"row":99,"column":64},"end":{"row":99,"column":75},"action":"remove","lines":["term_defini"],"id":1172},{"start":{"row":99,"column":64},"end":{"row":99,"column":79},"action":"insert","lines":["term_definition"]}],[{"start":{"row":99,"column":79},"end":{"row":99,"column":80},"action":"insert","lines":["="],"id":1173},{"start":{"row":99,"column":80},"end":{"row":99,"column":81},"action":"insert","lines":["t"]},{"start":{"row":99,"column":81},"end":{"row":99,"column":82},"action":"insert","lines":["e"]},{"start":{"row":99,"column":82},"end":{"row":99,"column":83},"action":"insert","lines":["r"]},{"start":{"row":99,"column":83},"end":{"row":99,"column":84},"action":"insert","lines":["m"]}],[{"start":{"row":99,"column":80},"end":{"row":99,"column":84},"action":"remove","lines":["term"],"id":1174},{"start":{"row":99,"column":80},"end":{"row":99,"column":95},"action":"insert","lines":["term_definition"]}],[{"start":{"row":99,"column":95},"end":{"row":99,"column":96},"action":"insert","lines":[","],"id":1175}],[{"start":{"row":99,"column":96},"end":{"row":99,"column":97},"action":"insert","lines":[" "],"id":1176}],[{"start":{"row":99,"column":43},"end":{"row":99,"column":44},"action":"insert","lines":["t"],"id":1177},{"start":{"row":99,"column":44},"end":{"row":99,"column":45},"action":"insert","lines":["e"]},{"start":{"row":99,"column":45},"end":{"row":99,"column":46},"action":"insert","lines":["r"]},{"start":{"row":99,"column":46},"end":{"row":99,"column":47},"action":"insert","lines":["m"]},{"start":{"row":99,"column":47},"end":{"row":99,"column":48},"action":"insert","lines":["s"]},{"start":{"row":99,"column":48},"end":{"row":99,"column":49},"action":"insert","lines":["="]},{"start":{"row":99,"column":49},"end":{"row":99,"column":50},"action":"insert","lines":["t"]}],[{"start":{"row":99,"column":50},"end":{"row":99,"column":51},"action":"insert","lines":["e"],"id":1178},{"start":{"row":99,"column":51},"end":{"row":99,"column":52},"action":"insert","lines":["r"]},{"start":{"row":99,"column":52},"end":{"row":99,"column":53},"action":"insert","lines":["m"]},{"start":{"row":99,"column":53},"end":{"row":99,"column":54},"action":"insert","lines":["s"]},{"start":{"row":99,"column":54},"end":{"row":99,"column":55},"action":"insert","lines":[","]}],[{"start":{"row":99,"column":55},"end":{"row":99,"column":56},"action":"insert","lines":[" "],"id":1179}],[{"start":{"row":97,"column":4},"end":{"row":97,"column":11},"action":"remove","lines":["results"],"id":1180},{"start":{"row":97,"column":4},"end":{"row":97,"column":5},"action":"insert","lines":["t"]},{"start":{"row":97,"column":5},"end":{"row":97,"column":6},"action":"insert","lines":["e"]},{"start":{"row":97,"column":6},"end":{"row":97,"column":7},"action":"insert","lines":["r"]},{"start":{"row":97,"column":7},"end":{"row":97,"column":8},"action":"insert","lines":["m"]},{"start":{"row":97,"column":8},"end":{"row":97,"column":9},"action":"insert","lines":["s"]}],[{"start":{"row":99,"column":109},"end":{"row":99,"column":125},"action":"remove","lines":[" results=results"],"id":1181},{"start":{"row":99,"column":108},"end":{"row":99,"column":109},"action":"remove","lines":[","]}],[{"start":{"row":97,"column":4},"end":{"row":97,"column":9},"action":"remove","lines":["terms"],"id":1182},{"start":{"row":97,"column":4},"end":{"row":97,"column":5},"action":"insert","lines":["r"]},{"start":{"row":97,"column":5},"end":{"row":97,"column":6},"action":"insert","lines":["e"]},{"start":{"row":97,"column":6},"end":{"row":97,"column":7},"action":"insert","lines":["s"]},{"start":{"row":97,"column":7},"end":{"row":97,"column":8},"action":"insert","lines":["u"]},{"start":{"row":97,"column":8},"end":{"row":97,"column":9},"action":"insert","lines":["l"]},{"start":{"row":97,"column":9},"end":{"row":97,"column":10},"action":"insert","lines":["t"]},{"start":{"row":97,"column":10},"end":{"row":97,"column":11},"action":"insert","lines":["s"]}],[{"start":{"row":99,"column":49},"end":{"row":99,"column":54},"action":"remove","lines":["terms"],"id":1183},{"start":{"row":99,"column":49},"end":{"row":99,"column":50},"action":"insert","lines":["r"]},{"start":{"row":99,"column":50},"end":{"row":99,"column":51},"action":"insert","lines":["e"]},{"start":{"row":99,"column":51},"end":{"row":99,"column":52},"action":"insert","lines":["s"]},{"start":{"row":99,"column":52},"end":{"row":99,"column":53},"action":"insert","lines":["u"]},{"start":{"row":99,"column":53},"end":{"row":99,"column":54},"action":"insert","lines":["l"]},{"start":{"row":99,"column":54},"end":{"row":99,"column":55},"action":"insert","lines":["t"]},{"start":{"row":99,"column":55},"end":{"row":99,"column":56},"action":"insert","lines":["s"]}],[{"start":{"row":98,"column":49},"end":{"row":99,"column":0},"action":"insert","lines":["",""],"id":1184},{"start":{"row":99,"column":0},"end":{"row":99,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":99,"column":4},"end":{"row":99,"column":8},"action":"remove","lines":["    "],"id":1185}],[{"start":{"row":99,"column":4},"end":{"row":99,"column":5},"action":"insert","lines":["p"],"id":1186},{"start":{"row":99,"column":5},"end":{"row":99,"column":6},"action":"insert","lines":["r"]},{"start":{"row":99,"column":6},"end":{"row":99,"column":7},"action":"insert","lines":["i"]},{"start":{"row":99,"column":7},"end":{"row":99,"column":8},"action":"insert","lines":["n"]},{"start":{"row":99,"column":8},"end":{"row":99,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":99,"column":9},"end":{"row":99,"column":11},"action":"insert","lines":["()"],"id":1187}],[{"start":{"row":99,"column":10},"end":{"row":99,"column":11},"action":"insert","lines":["r"],"id":1188},{"start":{"row":99,"column":11},"end":{"row":99,"column":12},"action":"insert","lines":["e"]},{"start":{"row":99,"column":12},"end":{"row":99,"column":13},"action":"insert","lines":["s"]},{"start":{"row":99,"column":13},"end":{"row":99,"column":14},"action":"insert","lines":["u"]},{"start":{"row":99,"column":14},"end":{"row":99,"column":15},"action":"insert","lines":["l"]},{"start":{"row":99,"column":15},"end":{"row":99,"column":16},"action":"insert","lines":["t"]},{"start":{"row":99,"column":16},"end":{"row":99,"column":17},"action":"insert","lines":["s"]}],[{"start":{"row":99,"column":16},"end":{"row":99,"column":17},"action":"remove","lines":["s"],"id":1189}],[{"start":{"row":99,"column":4},"end":{"row":100,"column":0},"action":"insert","lines":["",""],"id":1190},{"start":{"row":100,"column":0},"end":{"row":100,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":99,"column":4},"end":{"row":99,"column":5},"action":"insert","lines":["f"],"id":1191},{"start":{"row":99,"column":5},"end":{"row":99,"column":6},"action":"insert","lines":["o"]},{"start":{"row":99,"column":6},"end":{"row":99,"column":7},"action":"insert","lines":["r"]}],[{"start":{"row":99,"column":7},"end":{"row":99,"column":8},"action":"insert","lines":[" "],"id":1192},{"start":{"row":99,"column":8},"end":{"row":99,"column":9},"action":"insert","lines":["r"]},{"start":{"row":99,"column":9},"end":{"row":99,"column":10},"action":"insert","lines":["e"]},{"start":{"row":99,"column":10},"end":{"row":99,"column":11},"action":"insert","lines":["s"]},{"start":{"row":99,"column":11},"end":{"row":99,"column":12},"action":"insert","lines":["u"]},{"start":{"row":99,"column":12},"end":{"row":99,"column":13},"action":"insert","lines":["l"]},{"start":{"row":99,"column":13},"end":{"row":99,"column":14},"action":"insert","lines":["t"]},{"start":{"row":99,"column":14},"end":{"row":99,"column":15},"action":"insert","lines":["s"]}],[{"start":{"row":99,"column":15},"end":{"row":99,"column":16},"action":"insert","lines":[" "],"id":1193},{"start":{"row":99,"column":16},"end":{"row":99,"column":17},"action":"insert","lines":["i"]},{"start":{"row":99,"column":17},"end":{"row":99,"column":18},"action":"insert","lines":["n"]}],[{"start":{"row":99,"column":18},"end":{"row":99,"column":19},"action":"insert","lines":[" "],"id":1194},{"start":{"row":99,"column":19},"end":{"row":99,"column":20},"action":"insert","lines":["r"]},{"start":{"row":99,"column":20},"end":{"row":99,"column":21},"action":"insert","lines":["e"]}],[{"start":{"row":99,"column":20},"end":{"row":99,"column":21},"action":"remove","lines":["e"],"id":1195},{"start":{"row":99,"column":19},"end":{"row":99,"column":20},"action":"remove","lines":["r"]},{"start":{"row":99,"column":18},"end":{"row":99,"column":19},"action":"remove","lines":[" "]},{"start":{"row":99,"column":17},"end":{"row":99,"column":18},"action":"remove","lines":["n"]},{"start":{"row":99,"column":16},"end":{"row":99,"column":17},"action":"remove","lines":["i"]},{"start":{"row":99,"column":15},"end":{"row":99,"column":16},"action":"remove","lines":[" "]},{"start":{"row":99,"column":14},"end":{"row":99,"column":15},"action":"remove","lines":["s"]},{"start":{"row":99,"column":13},"end":{"row":99,"column":14},"action":"remove","lines":["t"]}],[{"start":{"row":99,"column":13},"end":{"row":99,"column":14},"action":"insert","lines":["t"],"id":1196}],[{"start":{"row":99,"column":14},"end":{"row":99,"column":15},"action":"insert","lines":[" "],"id":1197},{"start":{"row":99,"column":15},"end":{"row":99,"column":16},"action":"insert","lines":["i"]},{"start":{"row":99,"column":16},"end":{"row":99,"column":17},"action":"insert","lines":["n"]}],[{"start":{"row":99,"column":17},"end":{"row":99,"column":18},"action":"insert","lines":[" "],"id":1198},{"start":{"row":99,"column":18},"end":{"row":99,"column":19},"action":"insert","lines":["r"]},{"start":{"row":99,"column":19},"end":{"row":99,"column":20},"action":"insert","lines":["e"]},{"start":{"row":99,"column":20},"end":{"row":99,"column":21},"action":"insert","lines":["s"]},{"start":{"row":99,"column":21},"end":{"row":99,"column":22},"action":"insert","lines":["u"]},{"start":{"row":99,"column":22},"end":{"row":99,"column":23},"action":"insert","lines":["l"]},{"start":{"row":99,"column":23},"end":{"row":99,"column":24},"action":"insert","lines":["t"]},{"start":{"row":99,"column":24},"end":{"row":99,"column":25},"action":"insert","lines":["s"]}],[{"start":{"row":100,"column":4},"end":{"row":100,"column":8},"action":"insert","lines":["    "],"id":1199}],[{"start":{"row":99,"column":25},"end":{"row":99,"column":26},"action":"insert","lines":[":"],"id":1200}],[{"start":{"row":91,"column":20},"end":{"row":91,"column":33},"action":"remove","lines":["<search_text>"],"id":1201},{"start":{"row":91,"column":19},"end":{"row":91,"column":20},"action":"remove","lines":["/"]}],[{"start":{"row":97,"column":4},"end":{"row":98,"column":0},"action":"insert","lines":["",""],"id":1202},{"start":{"row":98,"column":0},"end":{"row":98,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":93,"column":4},"end":{"row":96,"column":84},"action":"remove","lines":["term_name = mongo.db.terms.find({\"term_name\": search_text})","    term_definition = mongo.db.terms.find({\"term_definition\": search_text})","    category_name =  mongo.db.categories.find({\"category_name\": search_text})","    mongo.db.terms.create_index([('term_name', 'text'),('term_definition', 'text')])"],"id":1203}],[{"start":{"row":95,"column":0},"end":{"row":95,"column":4},"action":"remove","lines":["    "],"id":1204},{"start":{"row":94,"column":4},"end":{"row":95,"column":0},"action":"remove","lines":["",""]},{"start":{"row":94,"column":0},"end":{"row":94,"column":4},"action":"remove","lines":["    "]},{"start":{"row":93,"column":4},"end":{"row":94,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":92,"column":11},"end":{"row":92,"column":22},"action":"remove","lines":["search_text"],"id":1205}],[{"start":{"row":94,"column":4},"end":{"row":94,"column":8},"action":"remove","lines":["    "],"id":1206},{"start":{"row":94,"column":0},"end":{"row":94,"column":4},"action":"remove","lines":["    "]},{"start":{"row":93,"column":34},"end":{"row":94,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":92,"column":11},"end":{"row":92,"column":12},"action":"insert","lines":["s"],"id":1207},{"start":{"row":92,"column":12},"end":{"row":92,"column":13},"action":"insert","lines":["e"]},{"start":{"row":92,"column":13},"end":{"row":92,"column":14},"action":"insert","lines":["a"]},{"start":{"row":92,"column":14},"end":{"row":92,"column":15},"action":"insert","lines":["r"]},{"start":{"row":92,"column":15},"end":{"row":92,"column":16},"action":"insert","lines":["c"]},{"start":{"row":92,"column":16},"end":{"row":92,"column":17},"action":"insert","lines":["h"]},{"start":{"row":92,"column":17},"end":{"row":92,"column":18},"action":"insert","lines":["_"]}],[{"start":{"row":92,"column":18},"end":{"row":92,"column":19},"action":"insert","lines":["t"],"id":1208},{"start":{"row":92,"column":19},"end":{"row":92,"column":20},"action":"insert","lines":["e"]},{"start":{"row":92,"column":20},"end":{"row":92,"column":21},"action":"insert","lines":["x"]},{"start":{"row":92,"column":21},"end":{"row":92,"column":22},"action":"insert","lines":["t"]}],[{"start":{"row":94,"column":4},"end":{"row":95,"column":21},"action":"remove","lines":["for result in results:","        print(result)"],"id":1209},{"start":{"row":94,"column":0},"end":{"row":94,"column":4},"action":"remove","lines":["    "]},{"start":{"row":93,"column":75},"end":{"row":94,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":95,"column":0},"end":{"row":96,"column":0},"action":"remove","lines":["",""],"id":1210}],[{"start":{"row":94,"column":58},"end":{"row":94,"column":110},"action":"remove","lines":["term_name=term_name, term_definition=term_definition"],"id":1211},{"start":{"row":94,"column":57},"end":{"row":94,"column":58},"action":"remove","lines":[" "]},{"start":{"row":94,"column":56},"end":{"row":94,"column":57},"action":"remove","lines":[","]}],[{"start":{"row":91,"column":20},"end":{"row":91,"column":21},"action":"insert","lines":[","],"id":1212}],[{"start":{"row":91,"column":21},"end":{"row":91,"column":22},"action":"insert","lines":[" "],"id":1213},{"start":{"row":91,"column":22},"end":{"row":91,"column":23},"action":"insert","lines":["m"]},{"start":{"row":91,"column":23},"end":{"row":91,"column":24},"action":"insert","lines":["e"]},{"start":{"row":91,"column":24},"end":{"row":91,"column":25},"action":"insert","lines":["t"]},{"start":{"row":91,"column":25},"end":{"row":91,"column":26},"action":"insert","lines":["h"]},{"start":{"row":91,"column":26},"end":{"row":91,"column":27},"action":"insert","lines":["o"]},{"start":{"row":91,"column":27},"end":{"row":91,"column":28},"action":"insert","lines":["d"]},{"start":{"row":91,"column":28},"end":{"row":91,"column":29},"action":"insert","lines":["s"]},{"start":{"row":91,"column":29},"end":{"row":91,"column":30},"action":"insert","lines":["="]}],[{"start":{"row":91,"column":30},"end":{"row":91,"column":32},"action":"insert","lines":["[]"],"id":1214}],[{"start":{"row":91,"column":31},"end":{"row":91,"column":33},"action":"insert","lines":["''"],"id":1215}],[{"start":{"row":91,"column":32},"end":{"row":91,"column":33},"action":"insert","lines":["P"],"id":1216},{"start":{"row":91,"column":33},"end":{"row":91,"column":34},"action":"insert","lines":["O"]},{"start":{"row":91,"column":34},"end":{"row":91,"column":35},"action":"insert","lines":["S"]},{"start":{"row":91,"column":35},"end":{"row":91,"column":36},"action":"insert","lines":["T"]}],[{"start":{"row":92,"column":24},"end":{"row":93,"column":0},"action":"insert","lines":["",""],"id":1217},{"start":{"row":93,"column":0},"end":{"row":93,"column":4},"action":"insert","lines":["    "]},{"start":{"row":93,"column":4},"end":{"row":93,"column":5},"action":"insert","lines":["q"]},{"start":{"row":93,"column":5},"end":{"row":93,"column":6},"action":"insert","lines":["u"]},{"start":{"row":93,"column":6},"end":{"row":93,"column":7},"action":"insert","lines":["e"]},{"start":{"row":93,"column":7},"end":{"row":93,"column":8},"action":"insert","lines":["r"]},{"start":{"row":93,"column":8},"end":{"row":93,"column":9},"action":"insert","lines":["y"]}],[{"start":{"row":93,"column":9},"end":{"row":93,"column":10},"action":"insert","lines":[" "],"id":1218},{"start":{"row":93,"column":10},"end":{"row":93,"column":11},"action":"insert","lines":["="]}],[{"start":{"row":93,"column":11},"end":{"row":93,"column":12},"action":"insert","lines":[" "],"id":1219},{"start":{"row":93,"column":12},"end":{"row":93,"column":13},"action":"insert","lines":["r"]},{"start":{"row":93,"column":13},"end":{"row":93,"column":14},"action":"insert","lines":["e"]},{"start":{"row":93,"column":14},"end":{"row":93,"column":15},"action":"insert","lines":["q"]},{"start":{"row":93,"column":15},"end":{"row":93,"column":16},"action":"insert","lines":["u"]},{"start":{"row":93,"column":16},"end":{"row":93,"column":17},"action":"insert","lines":["e"]},{"start":{"row":93,"column":17},"end":{"row":93,"column":18},"action":"insert","lines":["s"]},{"start":{"row":93,"column":18},"end":{"row":93,"column":19},"action":"insert","lines":["t"]},{"start":{"row":93,"column":19},"end":{"row":93,"column":20},"action":"insert","lines":["."]},{"start":{"row":93,"column":20},"end":{"row":93,"column":21},"action":"insert","lines":["f"]},{"start":{"row":93,"column":21},"end":{"row":93,"column":22},"action":"insert","lines":["o"]},{"start":{"row":93,"column":22},"end":{"row":93,"column":23},"action":"insert","lines":["r"]},{"start":{"row":93,"column":23},"end":{"row":93,"column":24},"action":"insert","lines":["m"]}],[{"start":{"row":93,"column":24},"end":{"row":93,"column":25},"action":"insert","lines":["."],"id":1220},{"start":{"row":93,"column":25},"end":{"row":93,"column":26},"action":"insert","lines":["g"]},{"start":{"row":93,"column":26},"end":{"row":93,"column":27},"action":"insert","lines":["e"]},{"start":{"row":93,"column":27},"end":{"row":93,"column":28},"action":"insert","lines":["t"]}],[{"start":{"row":93,"column":28},"end":{"row":93,"column":30},"action":"insert","lines":["()"],"id":1221}],[{"start":{"row":93,"column":29},"end":{"row":93,"column":31},"action":"insert","lines":["''"],"id":1222}],[{"start":{"row":93,"column":30},"end":{"row":93,"column":31},"action":"insert","lines":["q"],"id":1223},{"start":{"row":93,"column":31},"end":{"row":93,"column":32},"action":"insert","lines":["u"]},{"start":{"row":93,"column":32},"end":{"row":93,"column":33},"action":"insert","lines":["e"]},{"start":{"row":93,"column":33},"end":{"row":93,"column":34},"action":"insert","lines":["r"]},{"start":{"row":93,"column":34},"end":{"row":93,"column":35},"action":"insert","lines":["y"]}],[{"start":{"row":92,"column":11},"end":{"row":92,"column":22},"action":"remove","lines":["search_text"],"id":1224}],[{"start":{"row":94,"column":58},"end":{"row":94,"column":69},"action":"remove","lines":["search_text"],"id":1225},{"start":{"row":94,"column":58},"end":{"row":94,"column":59},"action":"insert","lines":["q"]},{"start":{"row":94,"column":59},"end":{"row":94,"column":60},"action":"insert","lines":["u"]},{"start":{"row":94,"column":60},"end":{"row":94,"column":61},"action":"insert","lines":["e"]},{"start":{"row":94,"column":61},"end":{"row":94,"column":62},"action":"insert","lines":["r"]},{"start":{"row":94,"column":62},"end":{"row":94,"column":63},"action":"insert","lines":["y"]}],[{"start":{"row":95,"column":56},"end":{"row":95,"column":57},"action":"insert","lines":[","],"id":1226}],[{"start":{"row":95,"column":57},"end":{"row":95,"column":58},"action":"insert","lines":[" "],"id":1227},{"start":{"row":95,"column":58},"end":{"row":95,"column":59},"action":"insert","lines":["q"]},{"start":{"row":95,"column":59},"end":{"row":95,"column":60},"action":"insert","lines":["u"]},{"start":{"row":95,"column":60},"end":{"row":95,"column":61},"action":"insert","lines":["e"]},{"start":{"row":95,"column":61},"end":{"row":95,"column":62},"action":"insert","lines":["r"]},{"start":{"row":95,"column":62},"end":{"row":95,"column":63},"action":"insert","lines":["y"]},{"start":{"row":95,"column":63},"end":{"row":95,"column":64},"action":"insert","lines":["="]},{"start":{"row":95,"column":64},"end":{"row":95,"column":65},"action":"insert","lines":["q"]}],[{"start":{"row":95,"column":65},"end":{"row":95,"column":66},"action":"insert","lines":["u"],"id":1228},{"start":{"row":95,"column":66},"end":{"row":95,"column":67},"action":"insert","lines":["e"]},{"start":{"row":95,"column":67},"end":{"row":95,"column":68},"action":"insert","lines":["r"]},{"start":{"row":95,"column":68},"end":{"row":95,"column":69},"action":"insert","lines":["y"]}]]},"ace":{"folds":[],"scrolltop":1237,"scrollleft":0,"selection":{"start":{"row":95,"column":69},"end":{"row":95,"column":69},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1565858755582,"hash":"1787fd4182e4046fc7ca0d02fdfb24a785a21749"}