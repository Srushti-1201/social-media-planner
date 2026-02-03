import { useState, useEffect } from 'react';
import {
  Container, Grid, Card, CardContent, CardActions, Typography,
  Button, Chip, Box, IconButton, Dialog, DialogTitle,
  DialogContent, DialogActions
} from '@mui/material';
import { Edit, Delete, Add } from '@mui/icons-material';
import { postsAPI } from '../services/api';
import { useNavigate } from 'react-router-dom';
import { format } from 'date-fns';

const PostList = () => {
  const [posts, setPosts] = useState([]);
  const [deleteDialog, setDeleteDialog] = useState({ open: false, id: null });
  const navigate = useNavigate();

  useEffect(() => {
    fetchPosts();
  }, []);

  const fetchPosts = async () => {
    try {
      const response = await postsAPI.getAll();
      setPosts(response.data);
    } catch (error) {
      console.error('Error fetching posts:', error);
    }
  };

  const handleDelete = async () => {
    try {
      await postsAPI.delete(deleteDialog.id);
      setDeleteDialog({ open: false, id: null });
      fetchPosts();
    } catch (error) {
      console.error('Error deleting post:', error);
    }
  };

  const getStatusColor = (status) => {
    const colors = {
      draft: 'default',
      scheduled: 'info',
      published: 'success',
      archived: 'warning'
    };
    return colors[status] || 'default';
  };

  return (
    <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 3 }}>
        <Typography variant="h4">Content Posts</Typography>
        <Button
          variant="contained"
          startIcon={<Add />}
          onClick={() => navigate('/posts/new')}
        >
          New Post
        </Button>
      </Box>

      <Grid container spacing={3}>
        {posts.map((post) => (
          <Grid item xs={12} sm={6} md={4} key={post.id}>
            <Card>
              {post.image_url && (
                <Box
                  component="img"
                  src={post.image_url}
                  alt={post.title}
                  sx={{ width: '100%', height: 200, objectFit: 'cover' }}
                />
              )}
              <CardContent>
                <Typography variant="h6" gutterBottom>
                  {post.title}
                </Typography>
                <Typography variant="body2" color="text.secondary" sx={{ mb: 2 }}>
                  {post.content.substring(0, 100)}...
                </Typography>
                <Box sx={{ display: 'flex', gap: 1, mb: 1 }}>
                  <Chip label={post.platform} size="small" color="primary" />
                  <Chip
                    label={post.status}
                    size="small"
                    color={getStatusColor(post.status)}
                  />
                </Box>
                {post.scheduled_time && (
                  <Typography variant="caption" display="block">
                    Scheduled: {format(new Date(post.scheduled_time), 'PPp')}
                  </Typography>
                )}
                <Typography variant="caption" display="block">
                  Engagement: {post.engagement_score}
                </Typography>
              </CardContent>
              <CardActions>
                <IconButton
                  size="small"
                  onClick={() => navigate(`/posts/edit/${post.id}`)}
                >
                  <Edit />
                </IconButton>
                <IconButton
                  size="small"
                  color="error"
                  onClick={() => setDeleteDialog({ open: true, id: post.id })}
                >
                  <Delete />
                </IconButton>
              </CardActions>
            </Card>
          </Grid>
        ))}
      </Grid>

      <Dialog open={deleteDialog.open} onClose={() => setDeleteDialog({ open: false, id: null })}>
        <DialogTitle>Confirm Delete</DialogTitle>
        <DialogContent>
          Are you sure you want to delete this post?
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setDeleteDialog({ open: false, id: null })}>Cancel</Button>
          <Button onClick={handleDelete} color="error">Delete</Button>
        </DialogActions>
      </Dialog>
    </Container>
  );
};

export default PostList;