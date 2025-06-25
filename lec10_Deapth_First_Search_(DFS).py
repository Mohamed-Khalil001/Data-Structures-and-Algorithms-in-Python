
















"""
        40
       /  \
     20    60
    / \    / \
  10  30  50 70

🧠 in_order Traversal Visualization :

🟩 in_order(40)
├── 🟨 in_order(20)
│   ├── 🟦 in_order(10) 
│   │   ├── ❌ in_order(None) ← يرجع
│   │   ├── ✅ print(10) 
│   │   └── ❌ in_order(None) ← يرجع
│   ├── ✅ print(20)
│   └── 🟦 in_order(30)
│       ├── ❌ in_order(None) ← يرجع
│       ├── ✅ print(30)
│       └── ❌ in_order(None) ← يرجع
├── ✅ print(40)
└── 🟨 in_order(60)
    ├── 🟦 in_order(50)
    │   ├── ❌ in_order(None) ← يرجع
    │   ├── ✅ print(50)
    │   └── ❌ in_order(None) ← يرجع
    ├── ✅ print(60)
    └── 🟦 in_order(70)
        ├── ❌ in_order(None) ← يرجع
        ├── ✅ print(70)
        └── ❌ in_order(None) ← يرجع

        10 20 30 40 50 60 70 (in order for order arranged )
        """

"""
     60
    /  \
  50    70

🌲 pre_order Traversal Visualization :

🟩 pre_order(60)
├── ✅ print(60)
├── 🟨 pre_order(50)
│   ├── ✅ print(50)
│   ├── ❌ pre_order(None) ← يرجع
│   └── ❌ pre_order(None) ← يرجع
└── 🟨 pre_order(70)
    ├── ✅ print(70)
    ├── ❌ pre_order(None) ← يرجع
    └── ❌ pre_order(None) ← يرجع

60 50 70 (pre order for copy tree  )

"""
"""
     60
    /  \
  50    70

🌲 post_order Traversal Visualization :

🟩 post_order(60)
├── 🟨 post_order(50)
│   ├── ❌ post_order(None) ← يرجع
│   ├── ❌ post_order(None) ← يرجع
│   └── ✅ print(50)
├── 🟨 post_order(70)
│   ├── ❌ post_order(None) ← يرجع
│   ├── ❌ post_order(None) ← يرجع
│   └── ✅ print(70)
└── ✅ print(60)

50 70 60 (post order _node print in the end )
 """