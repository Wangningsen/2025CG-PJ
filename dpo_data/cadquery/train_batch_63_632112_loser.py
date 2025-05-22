import cadquery as cq
w0=cq.Workplane('YZ',origin=(31,0,0))
r=w0.sketch().arc((2,-91),(6,-76),(21,-61)).arc((-68,-24),(2,-91)).assemble().push([(50,75)]).circle(26).push([(50.5,74.5)]).rect(7,33,mode='s').finalize().extrude(-62)