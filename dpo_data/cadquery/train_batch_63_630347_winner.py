import cadquery as cq
w0=cq.Workplane('YZ',origin=(0,0,0))
w1=cq.Workplane('YZ',origin=(-25,0,0))
r=w0.sketch().segment((29,47),(91,38)).segment((98,84)).segment((36,93)).close().assemble().finalize().extrude(-83).union(w0.sketch().push([(-46.5,-1)]).rect(61,48).push([(-46,-1)]).circle(3,mode='s').push([(43,26)]).rect(32,36).finalize().extrude(13)).union(w0.workplane(offset=83/2).moveTo(-62,-55).cylinder(83,38)).union(w1.workplane(offset=85/2).moveTo(57.5,55.5).box(85,3,85))