import cadquery as cq
w0=cq.Workplane('YZ',origin=(-5,0,0))
w1=cq.Workplane('YZ',origin=(-20,0,0))
r=w0.sketch().arc((-15,-8),(-58,-77),(3,-21)).arc((42,72),(-15,-8)).assemble().finalize().extrude(-39).union(w0.workplane(offset=33/2).moveTo(-74,0).cylinder(33,26)).union(w1.sketch().segment((36,-53),(52,-53)).segment((52,-17)).arc((96,0),(85,46)).arc((45,84),(52,33)).segment((52,0)).segment((36,0)).close().assemble().push([(65,16.5)]).rect(26,35,mode='s').finalize().extrude(64))