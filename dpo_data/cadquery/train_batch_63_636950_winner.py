import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-69))
r=w0.sketch().segment((-94,56),(-62,2)).segment((6,40)).arc((89,7),(12,51)).segment((-17,100)).close().assemble().finalize().extrude(56).union(w0.sketch().segment((32,-99),(41,-100)).segment((45,-71)).arc((54,2),(35,-70)).close().assemble().finalize().extrude(137))