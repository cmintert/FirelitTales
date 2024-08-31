from django.shortcuts import render, redirect
from .forms import NodeForm
from services.node_manager import NodeManager

def input_node(request):
    if request.method == 'POST':
        form = NodeForm(request.POST)
        if form.is_valid():
            manager = NodeManager()
            manager.create_node(
                name=form.cleaned_data['name'],
                label=form.cleaned_data['label'],
                attributes=form.cleaned_data['attributes'],
                relations=form.cleaned_data['relations'],
                description=form.cleaned_data['description'],
                created_by=request.user.username  # Assuming you store usernames
            )
            return redirect('landing_page')
    else:
        form = NodeForm()
    return render(request, 'input_node/input_node.html', {'form': form})
