import cadquery as cq
w0=cq.Workplane('YZ',origin=(68,0,0))
r=w0.sketch().push([(-75,-4)]).rect(50,90).push([(-93,31)]).circle(4,mode='s').finalize().extrude(-135).union(w0.sketch().segment((-99,31),(-77,-3)).segment((-9,56)).segment((-20,72)).segment((-41,60)).segment((-41,62)).segment((-44,62)).segment((-44,58)).close().assemble().push([(61,-33)]).circle(39).finalize().extrude(-40))