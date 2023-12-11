import React from 'react';
import axios from 'axios';

const SavePost = () => {
  const [savedPosts, setSavedPosts] = useState([]);

  useEffect(() => {
    const fetchSavedPosts = async () => {
      try {
        const response = await axiosReq.get("/saved-posts/");
        setSavedPosts(response.data);
      } catch (error) {
        console.error(error);
      }
    };

    fetchSavedPosts();
  }, []);


  return (
    <button onClick={handleSave}>
      Save
    </button>
  );
};

export default SavePost;