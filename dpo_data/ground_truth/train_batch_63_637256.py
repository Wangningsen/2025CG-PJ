import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,31,0))
r=w0.sketch().arc((-17,-20),(71,-67),(72,34)).segment((81,34)).segment((81,38)).arc((70,40),(60,44)).segment((60,39)).arc((31,41),(4,29)).arc((-95,44),(-17,-20)).assemble().finalize().extrude(-62)