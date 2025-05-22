import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,13))
r=w0.workplane(offset=-51/2).moveTo(35,-64).cylinder(51,36).union(w0.sketch().segment((-71,-65),(26,-65)).segment((9,-47)).segment((31,-26)).segment((48,-42)).segment((48,100)).segment((-71,100)).close().assemble().push([(-6,61)]).rect(38,12,mode='s').finalize().extrude(25))