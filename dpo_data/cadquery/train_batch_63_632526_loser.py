import cadquery as cq
w0=cq.Workplane('YZ',origin=(-10,0,0))
w1=cq.Workplane('XY',origin=(0,0,22))
r=w0.sketch().segment((-100,-31),(-98,-41)).segment((-93,-40)).segment((-93,-51)).segment((-49,-51)).segment((-49,-37)).segment((-47,-37)).segment((-49,-26)).segment((-49,-8)).segment((-93,-8)).segment((-93,-25)).segment((-95,-25)).segment((-95,-28)).segment((-97,-28)).segment((-95,-30)).close().assemble().push([(19,-28)]).circle(33).push([(88,31)]).circle(12).finalize().extrude(-63).union(w1.workplane(offset=39/2).moveTo(71,29).cylinder(39,2))