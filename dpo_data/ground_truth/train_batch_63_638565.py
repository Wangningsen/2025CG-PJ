import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,82))
w1=cq.Workplane('YZ',origin=(-19,0,0))
r=w0.sketch().push([(-41,43)]).circle(57).circle(27,mode='s').push([(22,-76.5)]).rect(152,47).finalize().extrude(-39).union(w0.workplane(offset=-16/2).moveTo(-41.5,43).box(77,38,16)).union(w1.workplane(offset=-41/2).moveTo(-36,-20).cylinder(41,62))