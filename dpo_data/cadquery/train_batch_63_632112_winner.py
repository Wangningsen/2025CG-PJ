import cadquery as cq
w0=cq.Workplane('YZ',origin=(31,0,0))
r=w0.sketch().arc((1,-91),(8,-73),(22,-60)).arc((-66,-21),(1,-91)).assemble().push([(50,75)]).circle(25).push([(50.5,75)]).rect(7,48,mode='s').finalize().extrude(-62)