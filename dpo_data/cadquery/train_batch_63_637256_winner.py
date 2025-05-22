import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,31,0))
r=w0.sketch().arc((-17,-19),(54,-73),(95,8)).segment((93,8)).segment((93,11)).arc((87,21),(79,30)).segment((81,38)).segment((60,43)).segment((58,39)).arc((30,41),(4,29)).arc((-95,45),(-17,-19)).assemble().finalize().extrude(-62)