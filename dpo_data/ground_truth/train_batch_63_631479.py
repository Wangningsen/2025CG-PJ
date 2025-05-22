import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,1))
r=w0.sketch().segment((-24,-80),(-23,-82)).segment((-23,-100)).segment((-8,-100)).segment((-8,-78)).segment((-7,-77)).segment((-8,-76)).segment((-8,-58)).segment((-23,-58)).segment((-23,-80)).close().assemble().push([(6,82)]).circle(18).push([(2,93)]).rect(2,6,mode='s').finalize().extrude(-2)