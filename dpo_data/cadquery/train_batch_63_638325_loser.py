import cadquery as cq
w0=cq.Workplane('YZ',origin=(17,0,0))
r=w0.sketch().arc((-53,6),(-1,-100),(46,13)).arc((-9,100),(-53,6)).assemble().push([(0,-34)]).circle(2,mode='s').finalize().extrude(-101).union(w0.sketch().push([(0,-34.5)]).rect(34,37).push([(0,-34)]).circle(16,mode='s').finalize().extrude(68))