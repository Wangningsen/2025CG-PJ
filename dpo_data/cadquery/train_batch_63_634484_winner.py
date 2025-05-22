import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,20))
w1=cq.Workplane('ZX',origin=(0,14,0))
r=w0.sketch().push([(-48,-21)]).circle(52).push([(-48.5,-20.5)]).rect(97,29,mode='s').finalize().extrude(43).union(w0.sketch().arc((98,21),(100,31),(98,41)).close().assemble().finalize().extrude(42)).union(w1.sketch().push([(-37,22.5)]).rect(52,23).push([(-42,20)]).circle(9,mode='s').push([(-27.5,20)]).rect(11,12,mode='s').finalize().extrude(59))