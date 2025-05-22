import cadquery as cq
w0=cq.Workplane('YZ',origin=(3,0,0))
r=w0.sketch().segment((-97,-66),(-97,-63)).segment((-86,-64)).segment((-86,-75)).arc((-67,-41),(-97,-66)).assemble().push([(97,73)]).circle(3).finalize().extrude(-5)