import cadquery as cq
w0=cq.Workplane('YZ',origin=(16,0,0))
r=w0.sketch().push([(31.5,-30.5)]).rect(47,77).push([(39,-40)]).circle(4,mode='s').finalize().extrude(-79).union(w0.sketch().push([(-56,25)]).circle(44).push([(60.5,-36.5)]).rect(11,65).reset().face(w0.sketch().arc((89,-67),(94,-63),(100,-59)).segment((100,-4)).segment((89,-4)).close().assemble()).finalize().extrude(47))