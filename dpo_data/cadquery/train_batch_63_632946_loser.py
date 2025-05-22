import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,9,0))
w1=cq.Workplane('ZX',origin=(0,-22,0))
r=w0.workplane(offset=79/2).moveTo(-40,14.5).box(74,89,79).union(w0.sketch().arc((17,-29),(12,-41),(24,-44)).close().assemble().reset().face(w0.sketch().segment((17,-28),(25,-43)).arc((29,-31),(17,-28)).assemble()).finalize().extrude(91)).union(w1.sketch().push([(28.5,-48.5)]).rect(97,21).push([(8.5,-42.5)]).rect(11,13,mode='s').finalize().extrude(-78))