import cadquery as cq
w0=cq.Workplane('YZ',origin=(7,0,0))
w1=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().segment((60,-47),(62,-51)).segment((82,-31)).segment((80,-29)).close().assemble().finalize().extrude(-29).union(w0.sketch().segment((-82,-95),(-68,-95)).arc((-62,-100),(-56,-95)).segment((-42,-95)).segment((-42,-85)).segment((-56,-85)).arc((-62,-80),(-68,-85)).segment((-82,-85)).close().assemble().push([(-62,-90)]).circle(4,mode='s').finalize().extrude(16)).union(w1.sketch().push([(-5,-3.5)]).rect(26,117).push([(-4,-40.5)]).rect(24,13,mode='s').finalize().extrude(-145))