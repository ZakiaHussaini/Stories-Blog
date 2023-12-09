import React from 'react';
import axios from 'axios';

const SavePost = ({ postId, onSave }) => {
  const handleSave = async () => {
    try {
      await axios.patch(`/api/posts/${postId}/save/`);
      onSave(postId); // Notify parent component that the post has been saved
    } catch (error) {
      console.log(error)
    }
  };

  return (
    <button onClick={handleSave}>
      Save
    </button>
  );
};

export default SavePost;