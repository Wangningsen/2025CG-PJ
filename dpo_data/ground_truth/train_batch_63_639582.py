import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,13,0))
w1=cq.Workplane('XY',origin=(0,0,55))
r=w0.sketch().push([(-55.5,-41.5)]).rect(61,41).push([(-4,-3)]).circle(13).finalize().extrude(-113).union(w0.workplane(offset=79/2).moveTo(75.5,62.5).box(21,53,79)).union(w1.sketch().arc((-79,1),(-60,-52),(-9,-28)).arc((4,-24),(15,-17)).segment((20,-17)).segment((20,-13)).arc((41,35),(20,84)).segment((20,87)).segment((15,87)).arc((-24,100),(-63,87)).segment((-67,87)).segment((-67,84)).arc((-88,45),(-79,1)).assemble().finalize().extrude(-138))