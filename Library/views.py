from django.shortcuts import render, redirect, get_object_or_404
from .models import Books, Category
from .forms import BookForm, CategoryForm
# Create your views here. -->

# Function-based view for index page
def index (request):
    # Check if request method is POST
    if request.method == 'POST':
        # Initialize forms for books and categories
        booksData = BookForm(request.POST, request.FILES)
        categoryData = CategoryForm(request.POST)
        # Check if books data is valid
        if booksData.is_valid():
            # Save books data
            booksData.save()
        # Check if category data is valid
        if categoryData.is_valid():
            # Save category data
            categoryData.save()

     # Get all books and categories from the database
    books = Books.objects.all()
    cat = Category.objects.all()
    num_books = Books.objects.filter(is_active=True).count()       
    # Create a context dictionary with books, categories, and empty forms
    context = {
        'books': books,
        'cat': cat,
        'form': BookForm(),
        'formCat': CategoryForm(),
        'num_books': num_books,
        'available': Books.objects.filter(status='Available').count(),
        'rented': Books.objects.filter(status='Rented').count(),
        'sold': Books.objects.filter(status='Sold').count(),
        

        
    }
    # Render the index.html template with the context
    return render(request, 'index.html', context)

# Function to display books and category form
def books(request):
    # Handle POST request
    if request.method == 'POST':
        # Form data processing
        category_data = CategoryForm(request.POST)
        # Check if form data is valid
        if category_data.is_valid():
            # Save form data
            category_data.save()

    # Fetch books and categories from the database
    search = Books.objects.all()
    cat = Category.objects.all()
    title = None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains=title)
        
    # Prepare context for the template
    context = {
        'search': search,
        'cat': cat,
        'formCat': CategoryForm(),
    }

    # Render the template
    return render(request, 'books.html', context)

# Function to delete a book object
def delete (request, id):
    # Get the book object or return 404 if not found
    book_id = get_object_or_404(Books, id=id)

    # If the request method is POST
    if request.method == 'POST':
        # Delete the book object
        book_id.delete()
        # Redirect to home page
        return redirect('/')
    # Render the delete.html template
    return render(request, 'delete.html')

# Function to update a book in the database
def update (request, id):
    # Get the book object with the given id
    book_id = Books.objects.get(id=id)

    # If the request method is POST
    if request.method == 'POST':
        # Create a BookForm object with the submitted data and save it
        editForm = BookForm(request.POST, request.FILES, instance=book_id)
        if editForm.is_valid():
            editForm.save()
            # Redirect to the home page
            return redirect('/')
    else:
        # Create a BookForm object with the book object as instance
        editForm = BookForm(instance=book_id)

    # Create a context dictionary with the editForm object
    context = {
        'editForm': editForm
    }    
    # Render the 'update.html' template with the context
    return render(request, 'update.html', context)
