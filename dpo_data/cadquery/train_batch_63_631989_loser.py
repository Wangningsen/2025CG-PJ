import cadquery as cq
w0=cq.Workplane('YZ',origin=(-25,0,0))
w1=cq.Workplane('XY',origin=(0,0,-49))
r=w0.sketch().segment((-67,29),(-37,13)).segment((-50,-14)).segment((-42,-19)).segment((-39,-14)).segment((-38,-14)).segment((-38,-100)).segment((57,-100)).segment((57,1)).segment((24,1)).segment((60,42)).segment((-13,100)).close().assemble().finalize().extrude(-7).union(w0.workplane(offset=57/2).moveTo(-2.5,15).box(95,76,57)).union(w1.sketch().push([(-12.5,38.5)]).rect(11,57).push([(-12,38)]).circle(6,mode='s').finalize().extrude(48))