/*// Function to add a new folder with delete and modify buttons
function addFolder() {
    const folderContainer = document.getElementById('folderContainer');
    const newFolder = document.createElement('div');
    newFolder.className = 'folder';
    const folderName = document.createElement('a');
    folderName.href = '#'; // Set the href attribute as needed
    folderName.innerText = 'New Folder';
    folderName.addEventListener('click', function(e) {
      e.preventDefault();
      addFile(newFolder);
    });
    newFolder.appendChild(folderName);
    folderContainer.appendChild(newFolder);
  }
  
  // Function to add a file to a folder
  function addFile(folder) {
    folder.innerHTML = ''; // Clear the folder content
    const fileInput = document.createElement('input');
    fileInput.type = 'text';
    const addFileBtn = document.createElement('button');
    addFileBtn.innerText = 'Add File';
    addFileBtn.addEventListener('click', function() {
      const fileName = fileInput.value;
      if (fileName.trim() !== '') {
        const fileContainer = document.createElement('div');
        fileContainer.className = 'file';
        const fileNameLink = document.createElement('a');
        fileNameLink.href = '#'; // Set the href attribute as needed
        fileNameLink.innerText = fileName;
        const deleteBtn = document.createElement('button');
        deleteBtn.className = 'deleteBtn';
        deleteBtn.innerText = 'Delete File';
        deleteBtn.addEventListener('click', function() {
          fileContainer.remove();
        });
        const modifyBtn = document.createElement('button');
        modifyBtn.className = 'modifyBtn';
        modifyBtn.innerText = 'Modify File';
        modifyBtn.addEventListener('click', function() {
          const newFileName = prompt('Enter the new name for the file:');
          if (newFileName) {
            fileNameLink.innerText = newFileName;
          }
        });
        fileContainer.appendChild(fileNameLink);
        fileContainer.appendChild(deleteBtn);
        fileContainer.appendChild(modifyBtn);
        folder.appendChild(fileContainer);
      }
    });
    folder.appendChild(fileInput);
    folder.appendChild(addFileBtn);
  }
  
  // Event listener for the "ADD FOLDER" button
  document.getElementById('addFolderBtn').addEventListener('click', addFolder);
  
*/

/*
function addFolder() {
    const folderContainer = document.getElementById('folderContainer');
    const newFolder = document.createElement('div');
    newFolder.className = 'folder';
    const folderName = document.createElement('a');
    folderName.href = '#'; // Set the href attribute as needed
    folderName.innerText = 'New Folder';
    const deleteBtn = document.createElement('button');
    deleteBtn.className = 'deleteBtn';
    deleteBtn.innerText = 'Delete Folder';
    deleteBtn.addEventListener('click', function() {
      folderContainer.removeChild(newFolder);
    });
    const modifyBtn = document.createElement('button');
    modifyBtn.className = 'modifyBtn';
    modifyBtn.innerText = 'Modify Folder';
    modifyBtn.addEventListener('click', function() {
      const newName = prompt('Enter the new name for the folder:');
      if (newName) {
        folderName.innerText = newName;
      }
    });
    newFolder.appendChild(folderName);
    newFolder.appendChild(deleteBtn);
    newFolder.appendChild(modifyBtn);
    folderContainer.appendChild(newFolder);
  }
  
  // Event listener for the "ADD FOLDER" button
  document.getElementById('addFolderBtn').addEventListener('click', addFolder);
*/