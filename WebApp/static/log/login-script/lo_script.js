console.log("script loaded")
function toggleImage() {
    const preview = document.getElementById('previewImage');
    const fileInput = document.getElementById('profile_picture');
    const uploadIcon = document.getElementById('uploadIcon');
    const profileStatus = document.getElementById('profile_picture_status');
    const defaultImagePath = document.getElementById('profilePicturePreview').getAttribute('data-default-image');

    // Check if the current image is the default image
    if (preview.src.includes(defaultImagePath)) {
        fileInput.click(); // Open file input to select a new image
    } else {
        // Reset to default image
        preview.src = defaultImagePath;
        uploadIcon.innerHTML = '<i class="fas fa-pencil-alt"></i>'; // Change back to "edit" icon
        fileInput.value = '';// Clear file input
        profileStatus.value = 'default';
        console.log("Profile status set to:", profileStatus.value);
    }
}

// Display the selected image in preview
function showPreview(event) {
    const preview = document.getElementById('previewImage');
    const uploadIcon = document.getElementById('uploadIcon');
    const profileStatus = document.getElementById('profile_picture_status');
    const file = event.target.files[0];

    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            preview.src = e.target.result; // Update preview with the new image
            uploadIcon.innerHTML = '<i class="fas fa-times"></i>'; // Change icon to "remove" (X)
            profileStatus.value = 'changed';
        }
        reader.readAsDataURL(file);
    }
}

