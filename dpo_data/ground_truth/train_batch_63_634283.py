import cadquery as cq
w0=cq.Workplane('YZ',origin=(3,0,0))
r=w0.sketch().arc((-97,-66),(-88,-64),(-88,-74)).arc((-66,-41),(-97,-66)).assemble().push([(97,73)]).circle(3).circle(2,mode='s').finalize().extrude(-5)