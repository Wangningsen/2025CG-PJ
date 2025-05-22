import cadquery as cq
w0=cq.Workplane('YZ',origin=(67,0,0))
r=w0.sketch().push([(-75,-4)]).rect(50,90).push([(-93.5,29)]).rect(7,2,mode='s').finalize().extrude(-135).union(w0.sketch().segment((-100,35),(-91,17)).segment((-11,54)).segment((-19,72)).close().assemble().push([(61,-33)]).circle(39).finalize().extrude(-40))