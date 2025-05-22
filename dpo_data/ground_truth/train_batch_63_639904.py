import cadquery as cq
w0=cq.Workplane('YZ',origin=(18,0,0))
r=w0.sketch().segment((10,36),(43,36)).segment((45,48)).arc((36,80),(51,50)).segment((48,36)).segment((73,36)).segment((73,92)).segment((10,92)).close().assemble().push([(21.5,43)]).rect(7,8,mode='s').finalize().extrude(-118).union(w0.workplane(offset=82/2).moveTo(-61,-80).cylinder(82,12))