import cadquery as cq
w0=cq.Workplane('YZ',origin=(6,0,0))
w1=cq.Workplane('ZX',origin=(0,-8,0))
r=w0.sketch().segment((-29,-50),(-14,-55)).arc((-8,-64),(3,-65)).segment((24,-69)).segment((29,-54)).segment((14,-49)).arc((8,-39),(-3,-39)).segment((-24,-35)).close().assemble().finalize().extrude(94).union(w1.sketch().segment((-23,-14),(7,-14)).arc((2,-75),(59,-98)).arc((61,-86),(61,-74)).segment((63,-74)).arc((65,-48),(63,-22)).segment((63,-21)).segment((68,-21)).arc((68,-13),(69,-5)).segment((69,36)).segment((-23,36)).close().assemble().finalize().extrude(36))