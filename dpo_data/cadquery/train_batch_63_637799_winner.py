import cadquery as cq
w0=cq.Workplane('YZ',origin=(45,0,0))
r=w0.sketch().segment((23,-45),(27,-45)).segment((27,-84)).segment((41,-84)).segment((41,-49)).segment((95,-49)).segment((95,66)).segment((23,66)).close().assemble().push([(37,-15)]).circle(6,mode='s').finalize().extrude(-89).union(w0.sketch().arc((-7,63),(-95,-27),(30,-37)).arc((97,41),(-7,63)).assemble().finalize().extrude(-28))