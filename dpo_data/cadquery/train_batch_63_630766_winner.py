import cadquery as cq
w0=cq.Workplane('YZ',origin=(24,0,0))
w1=cq.Workplane('XY',origin=(0,0,-12))
r=w0.sketch().push([(-18,-38)]).circle(25).push([(-18.5,-37.5)]).rect(29,11,mode='s').push([(-11,-23)]).circle(5,mode='s').finalize().extrude(76).union(w1.sketch().push([(-58,4)]).rect(84,78).circle(10,mode='s').finalize().extrude(75))