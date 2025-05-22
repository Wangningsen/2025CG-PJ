import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,19,0))
w1=cq.Workplane('YZ',origin=(-12,0,0))
r=w0.sketch().push([(-37,-39)]).rect(94,80).push([(-37,-39.5)]).rect(72,37,mode='s').finalize().extrude(-39).union(w0.sketch().segment((36,-80),(44,-80)).segment((44,-100)).segment((75,-100)).segment((75,-80)).segment((84,-80)).segment((84,-65)).segment((75,-65)).segment((75,-53)).segment((44,-53)).segment((44,-65)).segment((36,-65)).close().assemble().finalize().extrude(4)).union(w1.workplane(offset=112/2).moveTo(0,-32).cylinder(112,40))