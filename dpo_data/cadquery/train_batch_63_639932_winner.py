import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-14,0))
w1=cq.Workplane('XY',origin=(0,0,-37))
r=w0.sketch().push([(-20,-32)]).circle(26).push([(29,22.5)]).rect(42,27).finalize().extrude(-66).union(w0.sketch().segment((1,-16),(43,-72)).segment((100,-34)).segment((58,23)).close().assemble().finalize().extrude(5)).union(w1.sketch().segment((-1,11),(18,11)).segment((18,8)).segment((68,8)).segment((68,66)).segment((72,66)).segment((72,73)).segment((68,73)).segment((68,80)).segment((18,80)).segment((18,73)).segment((-1,73)).close().assemble().finalize().extrude(-63))