from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Node
from .forms import NodeForm

def input_node(request):
    if request.method == 'POST':
        form = NodeForm(request.POST)
        if form.is_valid():
            node = form.save(commit=False)
            node.node_created_by = request.user
            node.node_created_on = timezone.now()
            node.node_last_modified_by = request.user
            node.save(modified_by=request.user)
            return redirect('landing_page')
    else:
        form = NodeForm()
    return render(request, 'input_node/input_node.html', {'form': form})