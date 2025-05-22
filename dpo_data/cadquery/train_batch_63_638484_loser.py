import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,31,0))
r=w0.sketch().push([(-3,-60)]).circle(40).push([(-28.5,-51.5)]).rect(3,29,mode='s').reset().face(w0.sketch().segment((10,18),(39,17)).segment((43,99)).segment((14,100)).close().assemble()).finalize().extrude(-63)