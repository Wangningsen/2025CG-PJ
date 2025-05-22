import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-49))
r=w0.workplane(offset=95/2).moveTo(-32,-71).cylinder(95,29).union(w0.sketch().arc((-31,11),(-16,10),(-26,4)).arc((14,-10),(46,13)).segment((36,8)).segment((34,10)).segment((46,18)).segment((48,15)).arc((10,100),(-31,13)).arc((-30,12),(-31,11)).assemble().finalize().extrude(98))