import cadquery as cq
w0=cq.Workplane('YZ',origin=(-46,0,0))
w1=cq.Workplane('ZX',origin=(0,-49,0))
r=w0.sketch().segment((-33,-59),(-25,-59)).segment((-25,-60)).segment((65,-60)).segment((65,-59)).segment((74,-59)).segment((74,59)).segment((65,59)).segment((65,60)).segment((-25,60)).segment((-25,59)).segment((-33,59)).close().assemble().finalize().extrude(146).union(w1.sketch().push([(19,-87)]).circle(13).push([(19,-86.5)]).rect(10,15,mode='s').finalize().extrude(-25))