import cadquery as cq
w0=cq.Workplane('YZ',origin=(-3,0,0))
w1=cq.Workplane('ZX',origin=(0,-33,0))
r=w0.workplane(offset=-97/2).moveTo(-51,-35).cylinder(97,32).union(w0.sketch().arc((65,61),(-18,16),(75,37)).segment((78,37)).segment((78,61)).close().assemble().finalize().extrude(79)).union(w0.sketch().push([(-51,-35)]).circle(13).push([(26,-22)]).circle(57).finalize().extrude(103)).union(w1.workplane(offset=62/2).moveTo(-34.5,4.5).box(39,39,62))