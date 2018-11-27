from django.shortcuts import render

# Create your views here.
POSTS = [
    {
        'title': 'MilkyWay',
        'user': {
            'name':'Yojan',
            'picture':'https://scontent-atl3-1.xx.fbcdn.net/v/t1.0-9/17796718_10213034772769967_400751285401969937_n.jpg?_nc_cat=105&_nc_ht=scontent-atl3-1.xx&oh=adc1d6131114cccf6b165652066e2c10&oe=5CA3D203'
        },
        'photo': 'https://picsum.photos/200/200/?image=903',
        'description':'Asombroso el universo, nos hace dar cuenta de lo pequeños que somos pero tambien nos muestra lo mucho de lo que somos capaces.'
    },
    {
        'title': 'Olds',
        'user': {
            'name': 'Diana',
            'picture': 'https://scontent-atl3-1.xx.fbcdn.net/v/t1.0-9/25550428_10156057161433420_54604889915119125_n.jpg?_nc_cat=110&_nc_ht=scontent-atl3-1.xx&oh=bb7c60d1e4dc4b8b019585bc537de3d9&oe=5C749046'
        },
        'photo': 'https://picsum.photos/200/200/?image=111',
        'description':'Un clásico retocado.'
    }
]

def posts(request):
    return render(request,'posts/posts.html',{'posts':POSTS})
