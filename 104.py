import xml.dom.minidom

DOMTree = xml.dom.minidom.parse("D:/赵宇欣研究生/platform.xml")
collection = DOMTree.documentElement
# if collection.hasAttribute("shelf"):
#    print "Root element : %s" % collection.getAttribute("shelf")

permission = collection.getElementsByTagName("permission")
result = []
for p in permission:
	gid = []
	name =  p.getAttribute('name')
	group = p.getElementsByTagName("group")
	for g in group:
		gid.append(g.getAttribute('gid'))
	result.append([name, gid])
print(result)
