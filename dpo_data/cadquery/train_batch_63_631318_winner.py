import cadquery as cq
w0=cq.Workplane('YZ',origin=(19,0,0))
r=w0.sketch().arc((-37,3),(-6,-100),(36,-5)).arc((7,88),(-37,3)).assemble().push([(35,33)]).circle(16,mode='s').finalize().extrude(-46).union(w0.sketch().segment((-47,69),(12,-4)).segment((54,29)).segment((-8,100)).close().assemble().finalize().extrude(8))