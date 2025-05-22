import cadquery as cq
w0=cq.Workplane('YZ',origin=(68,0,0))
r=w0.sketch().push([(-75,-4)]).rect(50,90).push([(-94,31)]).circle(4,mode='s').finalize().extrude(-136).union(w0.sketch().segment((-89,19),(-87,16)).segment((-10,56)).segment((-19,72)).segment((-81,44)).arc((-80,31),(-89,19)).assemble().push([(61,-33)]).circle(39).finalize().extrude(-40))