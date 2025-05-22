import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-37,0))
r=w0.sketch().arc((51,47),(93,14),(59,55)).segment((59,47)).close().assemble().finalize().extrude(58).union(w0.sketch().push([(-81.5,-27)]).rect(37,64).push([(28,-29.5)]).rect(116,17).finalize().extrude(74))