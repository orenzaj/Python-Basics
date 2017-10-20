class JavaScriptObject(dict):
    def __getattribute__(self, item):
        try:
            return self[item]
        except KeyError:
            return super().__getattribute__(item)

jso = JavaScriptObject({"name" : "Flipsie"})
jso.language = "Python"


print(jso.name)
print(jso.language)
print(jso.fake)         #Double Error
