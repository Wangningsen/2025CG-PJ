import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-36,0))
r=w0.sketch().arc((51,47),(92,13),(59,55)).segment((59,47)).close().assemble().finalize().extrude(57).union(w0.sketch().push([(-81.5,-27)]).rect(37,64).push([(28,-29.5)]).rect(116,17).finalize().extrude(73))